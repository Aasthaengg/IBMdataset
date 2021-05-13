import math
A, B, C = map(int, input().split())

gcd = math.gcd(A, B)
print('YES' if C%gcd == 0 else 'NO')