N,K,Q=map(int,input().split())
p=[0]*N
s=0
for x in range(Q):
  A=int(input())
  p[A-1]+=1
  s+=1
for y in range(N):
  if K+p[y]-s>0:
    print("Yes")
  else:
    print("No")