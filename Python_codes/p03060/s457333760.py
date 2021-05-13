N=int(input())
L=[0]*N
V=list(map(int,input().split()))
C=list(map(int,input().split()))
for i in range(N):
  L[i]=V[i]-C[i]
L=sorted(L)
s=0
for i in range(N):
  if L[i]>=0:
    s+=L[i]
print(s)