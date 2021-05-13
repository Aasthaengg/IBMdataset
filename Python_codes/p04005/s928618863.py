import math
tmp = list(map(int, input().split()))
tmp.sort()
a = tmp[0]
b = tmp[1]
c = tmp[2]

if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    print(0)
else:

    print(abs(a * b * (c // 2) - (a * b * (math.ceil(c / 2)))))
