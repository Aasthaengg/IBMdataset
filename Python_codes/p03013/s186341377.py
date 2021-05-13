N,M=map(int,input().split())
L=[0]*N
c={}
mod=1000000007
for i in range(M):
  k=int(input())
  c[k]=0
for i in range(N):
  if i==0:
    L[i]=1
  elif i==1:
    if L[0]==0:
      L[i]=1
    else:
      L[i]=2
  else:
    L[i]=(L[i-1]+L[i-2])%mod
  if i+1 in c:
    L[i]=0
print(L[N-1])