import math
N = int(input())
for i in range(N,0,-1):
    if math.sqrt(i)%1 == 0:
        print(i)
        break