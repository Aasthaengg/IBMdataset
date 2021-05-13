import math
N = int(input())

if N%2 == 0:
    print(1/2)
else:
    print(math.ceil(N/2)/N)