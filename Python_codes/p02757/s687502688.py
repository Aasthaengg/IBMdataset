n,p=map(int,input().split())
s=input()
if 10%p==0:
  print(sum(i for i,x in enumerate(s,1) if int(x)%p==0))
  exit()
ans=0
u=0
d=1
l=[0]*p
l[0]=1
s=s[::-1]
for i in map(int,s):
  u=(u+i*d)%p
  l[u]+=1
  d=d*10%p
for i in l:
  ans+=i*(i-1)//2
print(ans)