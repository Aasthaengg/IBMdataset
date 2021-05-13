n,k=map(int,input().split())
N=[0]*(10**5+1)
for i in range(n):
  a,b=map(int,input().split())
  N[a]+=b
for i in range(10**5+1):
  k-=N[i]
  if k<=0:
    print(i)
    exit()