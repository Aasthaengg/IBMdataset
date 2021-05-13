import math

N, K = [int(x) for x in input().split()]

if K > math.ceil(N / 2):
    print('NO')
else:
    print('YES')