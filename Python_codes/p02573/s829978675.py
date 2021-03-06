import collections
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

class UnionFindPathCompression():
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [1]*n
        self.size = [1]*n
        

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return
        else:
            if self.rank[px] < self.rank[py]:
                self.parents[px] = py
                self.size[py] += self.size[px]
            else:
                self.parents[py] = px
                self.size[px] += self.size[py]
                #ランクの更新
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1


n,m = map(int,input().split())
ufpc = UnionFindPathCompression(n)
for _ in range(m):
    a,b = map(int,input().split())
    a,b=a-1,b-1
    ufpc.union(a,b)

for i in range(n):
    ufpc.find(i)

c = collections.Counter(ufpc.parents)
score_sorted = sorted(c.items(), key=lambda x:-x[1])
print(score_sorted[0][1])
