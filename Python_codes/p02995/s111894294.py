import math
a, b, c, d = map(int, input().split())
lcm = c * d // math.gcd(c, d)
multi_c = b // c - (a-1) // c
multi_d = b // d - (a-1) // d
multi_lcm = b // lcm - (a-1) // lcm
print(b - a + 1 - multi_c - multi_d + multi_lcm)