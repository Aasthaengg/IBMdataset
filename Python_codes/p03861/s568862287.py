a,b,x=map(int,input().split())

if a%x==0:
  a-=x
elif b%x==0:
  b+=x
elif b%x<a%x:
  b+=x
count=(b-a)//x
if count<0:
  count=0
print(count)