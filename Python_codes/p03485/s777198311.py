a,b=map(int, input().split())
m=0
if (a+b)%2!=0:
  m=1
print((a+b)//2+m)