import math
n = int(input())
if n % 2 == 0:
    print(int(n / 2))
elif n % 2 == 1:
    print(math.ceil(n / 2))