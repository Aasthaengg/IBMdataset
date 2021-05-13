import sys
sys.setrecursionlimit(10**7)

class UnionFind:
    def __init__(self,N):
        self.Parent = list(range(N))
    def get_Parent(self,n):
        if self.Parent[n] == n:return n
        p = self.get_Parent(self.Parent[n])
        self.Parent[n] = p
        return p
    def merge(self,x,y):
        x = self.get_Parent(x)
        y = self.get_Parent(y)
        if x!=y: self.Parent[y] = x
        return
    def is_united(self,x,y):
        return self.get_Parent(x)==self.get_Parent(y)

N,K,L = map(int,input().split())
PQ = [list(map(int,input().split())) for _ in [0]*K]
RS = [list(map(int,input().split())) for _ in [0]*L]

T1 = UnionFind(N)
T2 = UnionFind(N)
for p,q in PQ:
    p-=1;q-=1
    T1.merge(p,q)
for r,s in RS:
    r-=1;s-=1
    T2.merge(r,s)
P = {}
for i in range(N):
    p = (T1.get_Parent(i),T2.get_Parent(i))
    if not p in P:P[p] = []
    P[p].append(i)

ans = [0]*N
for v in P.values():
    s = len(v)
    for i in v:
        ans[i] = s
print(*ans)