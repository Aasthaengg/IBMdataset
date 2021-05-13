import math

all = list(map(int,input().split()))
a = all[0]
b = all[1]
c = all[2]
d = all[3]

if a >= 0 and c >= 0:
    print(b * d)
elif b <=0 and d <= 0:
    print(a * c)
elif a >= 0 and b >= 0 and c <= 0 and d <= 0:
    print(a * d)
elif a <= 0 and b <= 0 and c >= 0 and d >= 0:
    print(b * c)
elif a <= 0 and b >= 0 and c <= 0 and d >= 0:
    if a * c > b * d:
        print(a * c)
    else:
        print(b * d)
elif a <= 0 and b >= 0 and c <= 0 and d <= 0:
    if a * c > a * d:
        print(a * c)
    else:
        print(a * d)
elif a <= 0 and b <= 0 and c <= 0 and d >= 0:
    if a * c > b * c:
        print(a * c)
    else:
        print(b * c)
elif a <= 0 and b >= 0 and c >= 0 and d >= 0:
    if b * c > b * d:
        print(b * c)
    else:
        print(b * d)
elif a >= 0 and b >= 0 and c <= 0 and d >= 0:
    if a * d > b * d:
        print(a * d)
    else:
        print(b * d)