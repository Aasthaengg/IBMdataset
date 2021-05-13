class UnionFind():
    #https://note.nkmk.me/python-union-find/ 
    #note.nkmk.me  2019-08-18 
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

# 初期入力
import sys
input = sys.stdin.readline  #文字列では使わない

N,M = map(int, input().split())
bridge =[]
for i in range(M):
    a,b = map(int, input().split())
    bridge.append((a,b))

all =N*(N-1)//2 #行き来できる島の組み合わせ
ans =[0]*(M-1) +[all]
#print(ans)

#i 番目の橋が崩落した直後の不便さ＝i+1番目がまだ残っているときの不便さ
#   ⇒最後の橋から順番に作り、できた時の不便さ
uf =UnionFind(N)

for i in range(M-1,0,-1):

    a,b =bridge[i]
    #事前につながっているかどうかで場合分け
    if uf.same(a-1,b-1):
        ans[i-1] =ans[i]
    #くっつけてから変化分を引く
    else:
        x_a =uf.size(a-1)
        x_b =uf.size(b-1)
        connection_bfo =x_a*(x_a -1)//2 +x_b*(x_b -1)//2
        connection_aft =(x_a +x_b) *(x_a +x_b -1)//2 
        ans[i-1] =ans[i] -connection_aft +connection_bfo
        uf.union(a-1,b-1)
[print(i) for i in ans]
