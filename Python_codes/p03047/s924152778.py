N, K = map(int, input().split())

ans = 0

for i in range(N):
  if i+K <= N:
    ans += 1
  else:
    break

print(ans)