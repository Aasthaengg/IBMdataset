N, K = map(int, input().split()); res = 0
for i in range(K + 1, N + 1):
  if i == 1:
    res += 1
    continue
  res += (i - K) * (N // i) + max(N % i - K + 1, 0)
print(res)