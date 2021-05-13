import math
n = int(input())

if math.sqrt(n).is_integer():
    print(n)
else:
    tmp = math.floor(math.sqrt(n))
    print(tmp*tmp)