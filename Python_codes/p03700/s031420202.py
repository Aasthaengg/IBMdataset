N,A,B=map(int,input().split())
H=[int(input()) for i in range(N)]
L,R,M=0,10**9,0
A-=B
C=0
while L!=R:
  M=(L+R)//2
  C=0
  for i in range(N):
    C+=max(0,(H[i]-B*M+A-1)//A)
  if C>M:
    L=max(M,L+1)
  else:
    R=M
print(L)