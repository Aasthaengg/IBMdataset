a,b=map(int,input().split())
x=0
if a<=b:
  while b>0:
    x+=a*(10**(b-1))
    b-=1
else:
  while a>0:
    x+=b*(10**(a-1))
    a-=1
print(x)