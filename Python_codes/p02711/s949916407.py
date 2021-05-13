import math
N = int(input())
v = False
while N != 0:
    i = N - (N // 10) * 10
    v |= (i == 7)
    N //= 10
if v == True:
    print("Yes")
else:
    print("No")