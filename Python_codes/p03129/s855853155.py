import math

n, k = map(int, input().split())

ans = math.ceil(n/2)

if ans >= k:
    print('YES')
else:
    print('NO')