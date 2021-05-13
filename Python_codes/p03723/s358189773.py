a,b,c=map(int,input().split())
d=0
while(all([a%2==0,b%2==0,c%2==0])):
  x=b//2+c//2
  y=c//2+a//2
  z=a//2+b//2
  d+=1
  a=x
  b=y
  c=z
  if a==b==c:
    d=-1
    break
print(d)