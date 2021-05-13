N = int(input())
A = list(map(int,input().split()))
total = sum(A)
snk = A[0]
ari = total - snk
ans = abs(snk - ari)
for i in range(1,N-1):
  snk += A[i]
  ari -= A[i]
  ans = min(ans,abs(snk - ari))

print(ans)
