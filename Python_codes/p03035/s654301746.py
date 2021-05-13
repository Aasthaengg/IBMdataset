import math
a,b = map(int,input().split())
m = 0
if a >= 13:
    m = b
elif a >= 6 and a <=12:
    m = b / 2
print(math.floor(m))