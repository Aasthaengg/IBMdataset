from collections import Counter
import sys
input = sys.stdin.readline

# Union-Findデータ構造
class UnionFind:
    def __init__(self, numV):
        self.pars = list(range(numV))
        self.ranks = [0] * numV
    def getRoot(self, x):
        par = self.pars[x]
        if par != x:
            self.pars[x] = par = self.getRoot(par)
        return par
    def merge(self, x, y):
        x, y = self.getRoot(x), self.getRoot(y)
        if x == y: return
        if self.ranks[x] < self.ranks[y]:
            self.pars[x] = y
        else:
            self.pars[y] = x
            if self.ranks[x] == self.ranks[y]:
                self.ranks[x] += 1
    def isSame(self, x, y):
        return self.getRoot(x) == self.getRoot(y)
    def updatePars(self):
        for v in range(len(self.pars)):
            self.getRoot(v)

N, M = map(int, input().split())

UF = UnionFind(N)

for _ in range(M):
    A, B = map(int, input().split())
    A, B = A-1, B-1
    UF.merge(A, B)

UF.updatePars()

cnt = Counter(UF.pars)

ans = len(cnt.keys()) - 1
print(ans)
