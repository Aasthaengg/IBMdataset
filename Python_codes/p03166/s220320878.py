import sys
sys.setrecursionlimit(10**9)
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
  x,y = map(int,input().split())
  graph[x].append(y)
memo = [0]*(n+1)
done = [False]*(n+1)
for i in range(1,n+1):
  if len(graph[i]) == 0:
    done[i] = True
def cnt(i):
  if done[i]:
    return memo[i]
  else:
    l = []
    for j in graph[i]:
      l.append(cnt(j))
    memo[i] = max(l)+1
    done[i] = True
    return memo[i]
ans = [0]*n
for i in range(n):
  ans[i] = cnt(i+1)
print(max(ans))