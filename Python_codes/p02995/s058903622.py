import math
a, b, c, d = list(map(int, input().split()))

a_div_c = (a-1) // c
a_div_d = (a-1) // d
a_div_cd = (a-1) // (c * d // math.gcd(c, d))
b_div_c = b // c
b_div_d = b // d
b_div_cd = b // (c * d // math.gcd(c, d))

y = b - (b_div_c + b_div_d - b_div_cd)
x = (a - 1) - (a_div_c + a_div_d - a_div_cd)

print(y-x)


