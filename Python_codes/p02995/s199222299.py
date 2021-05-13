import math
a, b, c, d = map(int, input().split())
e = b - ((b // c) + (b // d) - (b // (c * d // math.gcd(c, d))))
f = (a - 1) - (((a - 1) // c) + ((a - 1) // d) - ((a - 1) // (c * d // math.gcd(c, d))))
ans = e - f
print(ans)