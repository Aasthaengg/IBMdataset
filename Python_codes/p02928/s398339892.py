N,K = map(int,input().split())
A = list(map(int,input().split()))
mod = 10**9+7
ans = 0
for i in range(N):
  f,g = 0,0
  for j in range(N):
    if A[i] > A[j]:
      g += 1
      if i < j:
        f += 1
  ans += ((f*K)+(g*(K*(K-1)//2)))%mod
print(ans%mod)