# https://atcoder.jp/contests/abc120/tasks/abc120_d


class UnionFind():

    def __init__(self,n):
        self.n = n
        self.parents = [-1]*n

    def find(self,x):
        if self.parents[x] < 0:
            return x
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

    def size(self, x):                                          # xの根のparent（= 要素数）を返す
        return -self.parents[self.find(x)]

    def members(self, x):                                       # xが属するグループの要素をリストとして返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):                                            # 全ての根の要素をリストとして返す
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):                                      # グループの数を返す
        return len(self.roots())

    def all_group_members(self):                                # {根:[根の子のリスト],...}をリストで返す
        return [list(self.members(r)) for r in self.roots()]





from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

data = [map(int, input().split()) for _ in range(M)]

tree = UnionFind(N)

res = []
inconv = N*(N-1)//2

for a, b in reversed(data):                                 # O(M)
    a -= 1
    b -= 1
    if tree.find(a) != tree.find(b):
        inconv -= tree.size(a)*tree.size(b)
        tree.union(a, b)
    res.append(inconv)

res.pop()                                   # 橋が落ちる前の最初の状態については出力しない

for a in reversed(res):
    print(a)

print(N*(N-1)//2)                           # 全ての道が切れた時の不便さを最後に追加

'''

4 5
1 2
3 4
1 3
2 3
1 4

'''