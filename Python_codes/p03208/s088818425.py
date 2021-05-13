
N, K = map(int, input().split())
h = []
ans = 10**9

for _ in range(N):
  h.append(int(input()))

h.sort()

for i in range(N-K+1):
  ans = min(ans, h[i+K-1] - h[i])

print(ans)