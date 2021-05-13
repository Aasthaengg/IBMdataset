N, K = map(int, input().split())
h = list(int(input()) for i in range(N))

h.sort()
ans = float('inf')

for i in range(N - K + 1):
  temp = h[i + K - 1] - h[i]
  if temp < ans:
    ans = temp

print(ans)
