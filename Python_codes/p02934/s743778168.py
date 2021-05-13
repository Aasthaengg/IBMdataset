N=int(input())
A=list(map(int,input().split()))
u=1
d=0
for i in range(N):
  u*=A[i]
for i in range(N):
  d+=u/A[i]
print(u/d)