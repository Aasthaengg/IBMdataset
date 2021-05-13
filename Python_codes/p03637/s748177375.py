import math

N = int(input())
a = list(map(int, input().split()))

N2 = 0
N4 = 0
oth = 0

for i in a:
    if i % 4 == 0:
        N4 += 1
    elif i % 2 == 0:
        N2 += 1
    else:
        oth += 1

if N2 == 0:
    if N4+1 >= oth:
        print("Yes")
    else:
        print("No")
else:
    if N4 >= oth:
        print("Yes")
    else:
        print("No")
