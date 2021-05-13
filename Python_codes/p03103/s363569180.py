N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(N)]
E.sort()

ans = 0

for i in range(N):
  if M - E[i][1] >= 0:
    ans += E[i][0] * E[i][1]
    M -= E[i][1]
  else:
    ans += E[i][0] * M
    break

print(ans)