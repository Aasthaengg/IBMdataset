from math import isqrt

N = int(input())

for x in range(isqrt(N), 0, -1):
    if not N % x:
        print(x + N // x - 2)
        exit()