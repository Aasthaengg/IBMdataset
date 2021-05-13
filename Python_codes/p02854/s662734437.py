N = int(input())
A = list(map(int, input().split()))
S = [0]*(N+1)
S[0] = 0
diff = float("INF")
idx = -1
m = sum(A)/2
for i in range(N):
  S[i+1] = S[i] + A[i]
  if abs(m - S[i+1]) < diff:
    diff = abs(m - S[i+1])
    idx = i+1
lsum = S[idx]
rsum = S[N]-S[idx]
print(abs(lsum-rsum))