n=int(input())
p=list(map(float,input().split()))
P=[[0]*(n+3) for i in range((n+1)//2)]
P[0][2]=1-p[0]
P[0][3]=p[0]
for i in range(1,(n-1)//2+1):
  a=(1-p[2*i-1])*(1-p[2*i])
  b=(1-p[2*i-1])*p[2*i]+p[2*i-1]*(1-p[2*i])
  c=p[2*i-1]*p[2*i]
  for j in range(2,n+3):
    P[i][j]=P[i-1][j]*a+P[i-1][j-1]*b+P[i-1][j-2]*c
ans=0
for i in range((n+1)//2):
  ans=ans+P[-1][-1-i]
print(ans)