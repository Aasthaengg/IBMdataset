import math

A, B, C = map(int, input().split())
X = math.gcd(A, B)
if C % X == 0:
    print('YES')
else:
    print('NO')