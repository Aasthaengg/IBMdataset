N, K = map(int, input().split())
H = [int(input()) for i in range(N)]
H.sort()

ans = 1000000000

for i in range(N-K+1):
  ans = min(ans, H[i+K-1] - H[i])

print(ans)