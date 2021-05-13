import math
n = int(input())
for i in reversed(range(n+1)):
    if round(math.sqrt(i))**2 == i:
        print(i)
        break