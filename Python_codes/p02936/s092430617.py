ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))
import sys

sys.setrecursionlimit(500000)

visited = set()

n,q = nm()

tval = [0]*n
t = [[] for _ in range(n)]

for i in range(n-1):
    a,b = nm()
    t[a-1].append(b-1)
    t[b-1].append(a-1)

for i in range(q):
    p,x = nm()
    tval[p-1] += x

ans = [0]*n
def dfs(num,val):
    visited.add(num)
    now = val+tval[num]
    ans[num] = now
    for nn in t[num]:
        if nn not in visited:
            dfs(nn,now)

dfs(0,0)

for i in ans:
    print(i)
