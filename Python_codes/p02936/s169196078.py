import sys
sys.setrecursionlimit(10**9)

n,q=map(int,input().split())
G=[[] for _ in range(n+1)]
for _ in range(n-1):
  a,b=map(int,input().split())
  G[a].append(b)
  G[b].append(a)

S=[0]*(n+1)
for _ in range(q):
  p,x=map(int,input().split())
  S[p]+=x

def dfs(now,prev=-1):
  for next in G[now]:
    if next==prev:
      continue
    S[next]+=S[now]
    dfs(next,now)

dfs(1)
print(*S[1:])