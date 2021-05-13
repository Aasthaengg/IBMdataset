import math
n = int(input())
while n > 0:
    if math.sqrt(n) == int(math.sqrt(n)):
        print(n)
        exit()
    n -= 1