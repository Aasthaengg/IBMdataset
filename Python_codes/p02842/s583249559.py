import math
a=int(input())
b=math.ceil(a/1.08)
c=math.floor(a/1.08)
if math.floor(b*1.08)==a:
    print(b)
elif math.floor(c*1.08)==a:
    print(c)
else:
    print(":(")