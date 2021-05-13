a,b=input().split()
c=int(a+b)
import math
d=math.sqrt(c)
if int(d)*int(d)==c:
    print("Yes")
else:
    print("No")