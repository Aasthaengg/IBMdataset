import math
s=int(input())
low=math.floor(s**0.5)
right=math.ceil(s**0.5)
if low==right:
    print(0,0,low,0,0,low)
else:
    print(0,0,right,right**2-s,1,right)