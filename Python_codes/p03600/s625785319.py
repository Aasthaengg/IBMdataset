import heapq
import sys
N = int(input())

r = [[1]*N for _ in range(N)]
g = [[]*N for _ in range(N)]
all = 0
for i in range(N):
  temp = list(map(int,(input().split())))
  g[i] = temp
  all += sum(temp)
#print(g,all)

for k in range(N):
  for i in range(N):
    for j in range(N):
      if g[i][j] > g[i][k] + g[k][j]:
        print("-1")
        sys.exit()
      elif g[i][j] == g[i][k] + g[k][j] and i != j and j != k and k != i:
        r[i][j] = 0
ans = 0
for i in range(N):
  for j in range(N):
    ans += g[i][j]*r[i][j]

ans = ans//2
print(ans)