import math
a,b=input().split()
c=int(a+b)
num=int(math.sqrt(c))
if num**2==c:
    print("Yes")
else:
    print("No")