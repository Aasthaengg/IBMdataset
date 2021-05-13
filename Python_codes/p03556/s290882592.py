import math
n = int(input())
for i in reversed(range(0,n + 1)):
    if (i ** .5).is_integer():
        print(i)
        break