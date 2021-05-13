import fractions
N,M=map(int,input().split())
S=input()
T=input()
L=N*M//fractions.gcd(N,M)
if S[::L//M]==T[::L//N]:
  print(L)
else:
  print(-1)