N = int(input())
arm = [list(map(int, input().split())) for _ in range(N)]
dist = [[0 for _ in range(3)] for _ in range(N)]

for i in range(N):
  dist[i][0] = arm[i][0] + arm[i][1]
  dist[i][1] = arm[i][0]
  dist[i][2] = arm[i][1]

dist.sort()

ans = 1
left = dist[0][1] + dist[0][2]
for i in range(1, N):
  if left <= dist[i][1] - dist[i][2]:
    ans += 1
    left = dist[i][1] + dist[i][2]

print(ans)