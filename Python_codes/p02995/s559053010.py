a, b, c, d = map(int, input().split())

import math
g = math.gcd(c, d)
l = int(c * d / g)

less_b = b - (b // c + b // d - b // l)
less_a = (a-1) - ((a-1)//c + (a-1) // d - (a-1)//l)
print(less_b-less_a)