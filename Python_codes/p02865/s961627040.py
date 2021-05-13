import math

N = int(input())
if (N%2 == 0):
    print(math.floor(N/2)-1)
else:
    print(math.floor(N/2))