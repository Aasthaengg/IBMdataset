N = int(input())
A = list(map(int, input().split()))
S = [0]*(N+1)
S[0] = 0
for i in range(N):
  S[i+1] = S[i] + A[i]

ans = float("INF")
for i in range(1, N+1):
  lsum = S[i]
  rsum = S[N]-S[i]
  ans = min(ans, abs(rsum-lsum))
  
print(ans)