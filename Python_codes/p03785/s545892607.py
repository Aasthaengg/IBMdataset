a,b,c=map(int,input().split())
l=sorted([int(input()) for i in range(a)])
ans=0
now=l[0]
cur=1
for i in range(1,a):
  x=l[i]
  if cur==b:
    now=x
    cur=1
    ans+=1
  elif x-now>c:
    now=x
    ans+=1
    cur=1
  else:
    cur+=1
print(ans+1)