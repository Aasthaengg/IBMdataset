sosuu=[1]*(10**5+1)
sosuu[0]=0
sosuu[1]=0
sosuu[2]=1
for i in range(2,318):
  for j in range(2*i,10**5+1,i):
    if sosuu[j]==1:
      sosuu[j]=0
nita=[]
for i in range(10**5+1):
  nita.append(sosuu[i])
nita[2]=0
for i in range(3,10**5+1,2):
  if sosuu[i]==1 and sosuu[(i+1)//2]!=1:
    nita[i]=0
c=[0]
for _ in range(1,10**5+1):
  c.append(c[-1]+nita[_])
q=int(input())
for _ in range(q):
  l,r=map(int,input().split())
  print(c[r]-c[l-1])
