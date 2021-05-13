import math
A,B,C,D = map(int,input().split())
a = math.ceil(A/D)
t = math.ceil(C/B)
if t<=a:
    print("Yes")
else:
    print("No")