import math

N = int(input())
for i in range(N, 0, -1):
    if math.sqrt(i) == int(math.sqrt(i)):
        print(i)
        break
