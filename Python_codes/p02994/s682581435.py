n,x=map(int,input().split())
a=abs(x)
l=[]
b=0
for i in range(1,n+1):
  l.append(i+x-1)
  if abs(x+i-1)<=a:
    a=abs(x+i-1)
    b=x+i-1
ans=0
for i in l:
  ans+=i
print(ans-b)