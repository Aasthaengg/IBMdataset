a, b, c = map(int,input().split())
import fractions
g = fractions.gcd(a, b)
if c%g == 0:
    print('YES')
else:
    print('NO')
