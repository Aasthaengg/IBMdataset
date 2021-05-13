import math
num=list(map(float,input().split(" ")))
x,y=math.fabs(num[0]-num[2]),math.fabs(num[1]-num[3])
ans=math.sqrt(x**2+y**2)
print(ans)
