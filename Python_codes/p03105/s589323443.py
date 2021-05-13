import math
a, b, c = map(int, input().split())

if a > b:
    print(0)
else :
    if b >= a * c:
        print(c)
    else :
        print(math.floor(b/a))