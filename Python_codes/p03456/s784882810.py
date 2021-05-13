import math

list = input().split()
a=list[0]
b=list[1]
c = a+b

if math.sqrt(int(c))%1 == 0:
    print("Yes")
else:
    print("No")
