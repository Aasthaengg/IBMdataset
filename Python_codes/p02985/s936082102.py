import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
mod = 10**9+7
sys.setrecursionlimit(4100000)
n,k = map(int,readline().split())
if n == 1:
  print(k%mod)
  exit()

g = [[] * n for i in range(n)]
for i in range(n-1):
    u, v = map(int,readline().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

ans = 1
used = [False]*n
def dfs(now,prev,p):
    global ans
    if k <= p:
      ans = 0
    ans *= k-p
    ans %= mod
    used[now] == True
    if all(used):
      return ans
    cnt = 1
    new = []
    for next in g[now]:
      if next == prev:
        cnt += 1
      else:
        new.append(next)
    for i,next in enumerate(new):
      dfs(next,now,cnt+i)
      
dfs(0,-1,0)
print(ans)
