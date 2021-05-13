N, K = map(int, input().split())
A = list(n for n in range(N+1))
ans = 0
for i in range(K,N+2):
  L = i*(i-1)//2
  R = i*(2*N+1-i)//2
  ans += (R-L+1)
print(ans%((10**9)+7))