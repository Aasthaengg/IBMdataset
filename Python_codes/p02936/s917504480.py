import sys
sys.setrecursionlimit(10**6)

#def input():
#  return sys.stdin.readline()[:-1]

n,q=map(int,input().split())
cnt=[0]*(n)
g=[[] for _ in range(n)]
for _ in range(n-1): #木グラフの隣接リストを作成
  a,b=map(int,input().split())
  g[a-1].append(b-1)
  g[b-1].append(a-1)
for _ in range(q):
    a , b = map(int,input().split())
    a = a - 1
    cnt[a] += b

def dfs(now,prev=-1):
  for next in g[now]:
    if next==prev:
      continue
      
    cnt[next]+=cnt[now]
    dfs(next,now)
dfs(0)
print(*cnt)
