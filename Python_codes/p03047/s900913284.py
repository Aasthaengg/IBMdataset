N, K = map(int, input().split())
ans = 0
for i in range(1, N + 1):
  if i + K - 1 <= N:
    ans += 1
  else:
    break

print('{}'.format(ans))

