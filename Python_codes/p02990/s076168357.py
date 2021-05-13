mod = 10**9+7
N, K = map(int, input().split())
print(N-K+1)
i = 2
C1 = N-K+1
C2 = 1
while i <= K:
  C1 *= ((N-K+1-(i-1))*pow(i, mod-2, mod))%mod
  C2 *= ((K-(i-1))*pow(i-1, mod-2, mod))%mod
  print((C1*C2)%mod)
  i += 1