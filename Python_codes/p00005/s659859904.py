import math
import sys
for line in sys.stdin.readlines():
    a, b = list(map(int, line.split()))
    print(f'{math.gcd(a,b)} {a*b//math.gcd(a,b)}')

