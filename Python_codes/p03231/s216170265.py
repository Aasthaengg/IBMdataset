import fractions

N,M = map(int,input().split())
S = list(input())
T = list(input())

g = fractions.gcd(N,M)

L = g * (N // g) * (M // g)

if S[0::N//g] == T[0::M//g]:
  print(L)
else:
  print(-1)



