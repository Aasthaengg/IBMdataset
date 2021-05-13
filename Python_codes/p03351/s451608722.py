import math
a,b,c,d = map(int,input().split())
if math.fabs(b-a)<=d and math.fabs(c-b)<=d:
    print("Yes")
elif math.fabs(c-a)<=d:
    print("Yes")
else:
    print("No")