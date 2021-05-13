N=int(input())
A=[int(input()) for _ in range(N)]

lmax=[0]*N
rmax=[0]*N

for i in range(1,N):
  lmax[i]=max(lmax[i-1],A[i-1])
for i in range(N-2,-1,-1):
  rmax[i]=max(rmax[i+1],A[i+1])

for i in range(N):
  print(max(lmax[i],rmax[i]))
