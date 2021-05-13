import sys
input=sys.stdin.buffer.readline
sys.setrecursionlimit(10**9)
class SegmentTree:
    #for pypy
    #treeは1-based-index
    __slots__=["size","func","default_val","tree","first_idx"]
    def __init__(self,initial_value_list,func,default_val,first_index=0):
        n=len(initial_value_list)
        self.first_idx=first_index
        self.size=1<<(n-1).bit_length()
        self.func=func#適用関数
        self.default_val=default_val#初期値
        self.tree=[default_val for i in range(2*self.size)]
        # 木の構築
        for i in range(n):
            d=[0]*26;d[initial_value_list[i]-97]=1
            self.tree[self.size+i]=d
        for i in range(self.size-1,0,-1):
            self.tree[i]=self.func(self.tree[2*i],self.tree[2*i+1])

    def update(self,k,x):
        k+=self.size-self.first_idx
        self.tree[k]=x
        while k>1:
            k>>=1
            self.tree[k]=self.func(self.tree[2*k],self.tree[2*k+1])
    def query(self, l, r):
        l+=self.size-self.first_idx
        r+=self.size-self.first_idx
        lret,rret=self.default_val,self.default_val
        while l<r:
            if l&1:
                lret=self.func(lret,self.tree[l])
                l+=1
            if r&1:
                r-=1
                rret=self.func(self.tree[r], rret) # モノイドでは可換律は保証されていないので演算の方向に注意
            l>>=1
            r>>=1
        return self.func(lret, rret)
n=int(input())
def add(x,y):
    v=[0]*26
    for i in range(26):
        v[i]=x[i]+y[i]
    return v
seg=SegmentTree(list(input().rstrip()),add,[0]*26,1)
q=int(input())

for i in range(q):
    a,s,d=input().split()
    if int(a)==1:
        s=int(s)
        v=[0]*26;v[int.from_bytes(d,'big')-97]+=1
        seg.update(s,v)
        
    else:
        r=seg.query(1,int(s))
        l=seg.query(1,int(d)+1)
        
        ans=0
        for i in range(26):
            if l[i]>r[i]:ans+=1
        print(ans)
