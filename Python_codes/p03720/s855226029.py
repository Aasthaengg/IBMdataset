n,m=map(int,input().split())
D=dict()
for i in range(n):
  D[i+1]=0
for i in range(m):
  a,b=map(int,input().split())
  D[a]+=1
  D[b]+=1
for i in range(1,n+1):
  print(D[i])