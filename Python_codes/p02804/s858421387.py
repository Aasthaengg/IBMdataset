N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
MOD = 10**9+7

#c[i] := (i)C(K-1)
c = [0] * (N+1)
#frac[i] = i!%MOD
frac = [1] * (N+1)
for i in range(1, N+1):
  frac[i] = (frac[i-1]*i)%MOD
for i in range(1, N+1):
  if(i >= K-1):
    c[i] = frac[i]*pow(frac[K-1], MOD-2, MOD)*pow(frac[i-K+1], MOD-2, MOD)%MOD

  
ans = 0
for i in range(N):
  ans = (ans + A[i]*c[i])%MOD
for i in range(N):
  ans = (ans - A[i]*c[N-i-1])%MOD
  
print(ans)