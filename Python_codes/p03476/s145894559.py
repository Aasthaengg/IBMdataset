INF=10**5+1
p=[1]*INF
for i in range(2,INF):
  if p[i]:
    for j in range(2*i,INF,i):p[j]=0
p[0],p[1]=0,0
q=[0]*INF
for i in range(INF):
  if i%2==0:continue
  if p[i]*p[(i+1)//2]:q[i]=1
for i in range(1,INF):
  q[i]+=q[i-1]
n=int(input())
for _ in range(n):
  l,r=map(int,input().split())
  print(q[r]-q[l-1])