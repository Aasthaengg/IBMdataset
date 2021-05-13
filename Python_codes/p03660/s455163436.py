import sys
input = sys.stdin.readline

n = int(input())
T = [[] for _ in range(n)]
for _ in range(n-1):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  T[a].append(b)
  T[b].append(a)
def dfs(v):
  dist = [-1]*n
  dist[v] = 0
  stack = [v]
  while stack:
    nv = stack.pop()
    for i in T[nv]:
      if dist[i] == -1:
        dist[i] = dist[nv] + 1
        stack.append(i)
  return dist
B = dfs(0)
W = dfs(n-1)
cnt_b, cnt_w = 0, 0
for i in range(n):
  if B[i] <= W[i]:
    cnt_b += 1
  else:
    cnt_w += 1
if cnt_b > cnt_w:
  print("Fennec")
else:
  print("Snuke")