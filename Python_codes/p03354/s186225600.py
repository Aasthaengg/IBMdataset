N,M = map(int,input().split())

class UnionFind:
    def __init__(self, n):
        #ノード数nの配列を作る
        #親の番号を格納する
        #-> 自分が根だった場合は、-(その集合のサイズ)とする
        #作るときはparentの値を全て-1にする
        #こうすると全てバラバラになる
        self.parent = [-1 for _ in range(n)]
        self.n = n
    def root(self, x):
        #要素xの根の番号を返す
        if self.parent[x] < 0:
            # 自分が根
            return x
        # 要素xの親を要素xの根に変えておく(付け替える)
        # 次の呼び出しが早くなる
        self.parent[x] = self.root(self.parent[x])
        return self.parent[x]
    def size(self, x):
        #要素xの所属するグループの頂点数を調べる
        #根のparentにサイズが格納されている
        return -self.parent[self.root(x)]
    def merge(self, x, y):
        #xとyを結合する
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        #大きい方(x)に小さい方(y)をくっつけたい
        if self.parent[x] > self.parent[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        return True
    def issame(self, x, y): #same(x,y): xとyが同じグループにあるならTrue
        return self.root(x) == self.root(y)
    def family(self,x): # xが属する連結集合を返す
        return [i for i in range(self.n) if self.issame(i,x)]
    def maximum(self): # 連結最大集合を返す
        return self.family(self.parent.index(min(self.parent)))
    def all_family(self): # 根集合P, 子集合の集合C(C[P[i]]にはiを根とする子集合が入る)
        P = {} # 根のindexの集合はP.keys()で取得できる．これは根iが何番目の根かを返すdict
        now = 0
        for i in range(self.n):
            if self.parent[i] < 0:
                P[i] = now
                now += 1
        C = [[] for _ in range(len(P))] # P[i]
        for i in range(self.n):
            C[P[self.root(i)]].append(i)
        return P,C


p = list(map(int,input().split()))
UF = UnionFind(N)
for i in range(M):
    x,y = map(int,input().split())
    UF.merge(x-1,y-1)

ans = 0
_,C = UF.all_family()
for i in range(len(C)):
    S = C[i]
    T = [p[i]-1 for i in S]
    ans += len(set(S).intersection(set(T)))

print(ans)