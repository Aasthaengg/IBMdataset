import math
x,y = map(int,input().split())
lcm = (x*y)//math.gcd(x,y)
flag = False
for i in range(x,lcm):
  if i%x==0 and i%y!=0:
    flag=True
    print(i)
    break
if not flag:
  print(-1)