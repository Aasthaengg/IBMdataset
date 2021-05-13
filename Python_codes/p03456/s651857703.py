from math import sqrt
a, b = map(str, input().split())
if sqrt(int(a+b)) % 1 == 0:
    print("Yes")
else:
    print("No")