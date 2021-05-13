import sys

N,K=map(int,input().split())
D=dict()
for i in range(N):
  a,b=map(int,input().split())
  try:
    D[a]+=b
  except:
    D[a]=b

D=sorted(D.items(),key=lambda x:x[0])


for k,v in D:
  K-=v
  if K<=0:
    print(k)
    break