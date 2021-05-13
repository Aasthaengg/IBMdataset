import math

D, N = map(int, input().split(' '))

if N == 100:
    N = 101

print(int(math.pow(100, D)) * N)