import math

a, b, c, d = map(int, input().split())
lcm_cd = c * d // math.gcd(c, d)

ans_lt_b = b - (b // c + b // d - b // lcm_cd)
ans_lt_a = (a - 1) - ((a - 1) // c + (a - 1) // d - (a - 1) // lcm_cd)
print(ans_lt_b - ans_lt_a)
