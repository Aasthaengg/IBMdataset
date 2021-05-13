N, K = map(int, input().split())
x = list(map(int, input().split()))
ans = 10**9
for i in range(N - K + 1):
  cost1 = abs(x[i]) + abs(x[i + K - 1] - x[i])
  if cost1 < ans:
    ans = cost1
  cost2 = abs(x[i + K - 1]) + abs(x[i + K - 1] - x[i])
  if cost2 < ans:
    ans = cost2
print(ans)
