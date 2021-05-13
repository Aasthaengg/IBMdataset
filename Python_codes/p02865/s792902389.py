import math
n = int(input())
x = math.sqrt(n)
if n == 1:
    print(0)
elif n % 2 == 1:
    print(math.floor(n/2))
elif n % 2 == 0:
    print(round(n/2)-1)