class UnionFind():
    def __init__(self, n):       #(要素数)の分だけリストを作る
        self.n = n               #負の数なら親、正の数なら親のノード番号を入力
        self.parents = [-1]*n    #負の数の絶対値はそのグループに属する要素数を意味する
   
    #xが属する親番号を返す
    def find(self, x):
        if self.parents[x-1] < 0:
            return x
        else:
            self.parents[x-1] = self.find(self.parents[x-1])
            return self.parents[x-1]
    
    #xとyに関係があるとき、xの属するグループとyの属するグループ統合する
    def union(self, x, y):
        x = self.find(x) #xの親番号を返す
        y = self.find(y) #yの親番号を返す

        if x == y: return
        else:
            #xに属するグループ数の方が大きいようにする
            if self.parents[x-1] > self.parents[y-1]:
                x, y = y, x
            self.parents[x-1] += self.parents[y-1]
            self.parents[y-1] = x 

    #xの属するグループの要素数を返す
    def size(self, x):
        return -self.parents[self.find(x)-1]
    
    #xとyが等しいかどうか
    def same(self, x, y):
        return self.find(x) == self.find(y)

    #xの属するグループの要素を返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    #親となる要素だけを返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    #グループの数を返す
    def group_count(self):
        return len(self.roots())

N, M = map(int, input().split())
uf = UnionFind(N)
for _ in range(M):
    A,B = map(int, input().split())
    uf.union(A,B)
parents = uf.roots()
ans = 0
for p in parents:
    ans = max(ans, uf.size(p))
print(ans)
