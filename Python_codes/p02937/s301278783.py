from bisect import *
S=input()
T=input()
N=len(S)
M=len(T)
O=ord('a')
X=[[0]*26 for i in range(N+1)]
Y=[[] for i in range(26)]
for i in range(N):
  Y[ord(S[i])-O].append(i)
for i in range(N):
  Y[ord(S[i])-O].append(N+i)
for i in range(M):
  if len(Y[ord(T[i])-O])==0:
    print(-1)
    exit()
for i in range(-1,N):
  for j in range(26):
    if len(Y[j]):
      X[i][j]=Y[j][bisect_right(Y[j],i)]
P=0
Z=-1
for i in range(M):
  P+=X[Z][ord(T[i])-O]-Z
  Z=X[Z][ord(T[i])-O]
  if Z>=N:
    Z-=N
print(P)