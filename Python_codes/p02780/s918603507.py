N, K = map(int, input().split())
P = list(map(int, input().split()))

ans = 0
P_sum = 0

for i in range(N):
  P[i] = (P[i] + 1) / 2

for j in range(K):
  P_sum += P[j]

ans = P_sum
for t in range(K, N):
  P_sum -= P[t - K]
  P_sum += P[t]
  ans = max(ans, P_sum)

print(ans)