# Union Find木の問題である

# 次のURLを参照して解いた
# http://at274.hatenablog.com/entry/2018/02/02/173000

class UnionFind():
    
    def __init__(self, n):
        # 各数字の親を管理するためのリストを作成する
        self.par = [i for i in range(n+1)]
        
        # 木の高さを管理するリストを用意する
        self.rank = [0] * (n+1)
    
    # 各数字の木の根が同じかどうかをチェックする
    def find(self, x):
        # 根である場合はその数字を返す
        if self.par[x] == x:
            return x
        # 違う場合は再帰関数を用いて根を返す
        # ただしこのままでは木が縦長の場合に検索の手間がかかる
        # 親を順に書き換えていく必要がある
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    
    # 根が同一かどうかを判定する
    def same_check(self, x, y):
        return self.find(x) == self.find(y)
    
    # 木どうしを結合するUnionの実装
    # 木の高さをなるべく低くするために、木が低い方の根から、高い方の根に辺を張る

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        # 木の高さを比較する
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
        
            # 木の高さが同じ場合は片方を1増やす
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


n, m = map(int, input().split())
P = list(map(int, input().split()))
XY = []
ans = 0

for _ in range(m):
    xy = list(map(int, input().split()))
    XY.append(xy)

UF = UnionFind(n)
for i in range(m):
    UF.union(P[XY[i][0]-1], P[XY[i][1]-1])

for j in range(n):
    if UF.same_check(j+1, P[j]):
        ans += 1

print(ans)