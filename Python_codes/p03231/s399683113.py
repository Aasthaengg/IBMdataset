from math import gcd
N,M=list(map(int, input().split()))
S=input()
T=input()
g=gcd(N,M)
l=N*M//g
n=l//N
m=l//M
for i in range(0,l,n):
  if i%m==0:
    if S[i//n]!=T[i//m]:
      print(-1)
      exit()
else:
  print(l)