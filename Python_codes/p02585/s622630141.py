#D
class UnionFind():
    # https://www.slideshare.net/chokudai/union-find-49066733
    # 作りたい要素数nで初期化
    # 使用するインスタンス変数の初期化
    def __init__(self, n):
        self.n = n
        # root[x]<0ならそのノードが根かつその値が木の要素数
        # rootノードでその木の要素数を記録する
        # root[x]>=0の場合は、特に直接的な意味を持たない気がする。計算に寄与するので意味はあるのだろうが。
        self.root = [-1]*(n+1)
        # 木をくっつける時にアンバランスにならないように調整する
        # 無結合の時はRank=0,結合して1つ木が深くなると根がRank+=1
        self.rnk = [0]*(n+1)

    # ノードxのrootノードを見つける
    #
    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            # ここで代入しておくことで、後の繰り返しを避ける
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]

    # 木の併合、入力は併合したい各ノード
    def Unite(self, x, y):
        # 入力ノードのrootノードを見つける
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        # すでに同じ木に属していた場合
        if(x == y):
            return
        # 違う木に属していた場合rnkを見てくっつける方を決める
        # (1)xのランクの方が大きい(位置が深い)場合
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x

        # (2)yのランクの方が大きい(位置が深い)場合 or 等しい場合
        # また等しい場合、引数の2つめのyの方のランクを1つ増やす
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            # rnkが同じ（深さに差がない場合）は1増やす
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1

    # xとyが同じグループに属するか判断
    # Return: True or False
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    # ノードxが属する木のサイズを返す
    def Count(self, x):
        return -self.root[self.Find_Root(x)]
###################################################################    
N,K=map(int,input().split())
UN=UnionFind(N)
P=list(map(int,input().split()))
C=list(map(int,input().split()))
for i,num in enumerate(P):
    UN.Unite(i+1,num)
root=set()
loop_score=dict()
loop_len=dict()

#print(UN.root)
for i,node in enumerate(UN.root):
    if i==0:
        pass
    else:
        if node<0:
            #print(i,"is root")
            root.add(i)
            score=0
            ini=i
            leng=0
            while True:
                ret=P[ini-1]
                score += C[ret-1]
                leng +=1
                if ret==i:
                    break
                else:
                    ini=ret
            loop_score[i]=score
            loop_len[i] = leng
            
#print(loop_score)
#print(loop_len)

ans_list=[]
ans=float("-inf")

for i in range(1,N+1):
    t=K
    p=UN.Find_Root(i)
    
    
    #ループした方がいいかの確認
    if loop_score[p]>0:
        tmp=0
        pos=i
        tmp += ((t//loop_len[p])-1)*loop_score[p]
        if tmp>0:
            ans=max(tmp,ans)
        t = (t%loop_len[p])+loop_len[p]
        for j in range(t):
            pos = P[pos-1]
            tmp += C[pos-1]
            ans=max(tmp,ans)

    else:
        tmp=0
        pos=i
        
        for j in range(min(t,loop_len[p]-1)):
            pos = P[pos-1]
            tmp += C[pos-1]
            ans=max(tmp,ans)
    
print(ans)