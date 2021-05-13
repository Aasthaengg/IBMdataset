from fractions import gcd
N,M=map(int,input().split())
S=input()
T=input()
L=N*M//gcd(N,M)
p=[]
q=[]

if S[::L//M]==T[::L//N]:
  print(L)
else:
  print(-1)
