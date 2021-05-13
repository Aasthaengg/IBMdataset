n,m=map(int,input().split())
count=0
s=[0]*(n+1)
L=0
R=10**5
 
for i in range(m):
  l,r=map(int,input().split())
  L=max(l,L)
  R=min(r,R)
  
if (R-L+1)>=0:
  print(R-L+1)
else:
  print(0)