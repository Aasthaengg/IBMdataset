import sys
S=sys.stdin.readlines()
N,A,B=map(int,S[0].split())
H=[int(S[i+1]) for i in range(N)]
L,R=0,10**9
M=0
Z=0
A-=B
while R>L:
  M=(L+R)//2
  Z=0
  for i in range(N):
    Z+=max((H[i]-B*M+A-1)//A,0)
  if Z>M:
    L=max(L+1,M)
  else:
    R=M
print(R)