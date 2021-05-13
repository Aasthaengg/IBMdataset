import sys
input = sys.stdin.readline
n = int(input())
dist = [list(map(int,input().split())) for i in range(n)]
ans = 0
for arr in dist:
  ans += sum(arr)

for i in range(n):
  for j in range(n):
    for k in range(n):
      if i != j and j != k and k != i:
        if dist[i][k]+dist[k][j] == dist[i][j] and dist[i][k] != 0 and dist[k][j] != 0:
          ans -= dist[i][j]
          break
        elif dist[i][k]+dist[k][j] < dist[i][j] and dist[i][k] != 0 and dist[k][j] != 0:
          print(-1)
          exit()
print(ans//2)