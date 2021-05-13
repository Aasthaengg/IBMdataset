import sys
sys.setrecursionlimit(10**7)

def dfs(x):
    seen[x]=1
    for nx in lis[x]:
        if seen[nx]==0:
            psum[nx]=psum[x]+plis[nx]
            dfs(nx)

n,q=map(int,input().split())

lis=[[] for i in range(n)]

for _ in range(n-1):
    ai,bi=map(lambda x:int(x)-1,input().split())
    lis[ai].append(bi)
    lis[bi].append(ai)

plis=[0 for i in range(n)]

for _ in range(q):
    pi,xi=map(int,input().split())
    plis[pi-1]+=xi

seen=[0 for _ in range(n)]
psum=[0 for _ in range(n)]
psum[0]=plis[0]

dfs(0)

print(*psum)