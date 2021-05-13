a, b, c, d = map(int, input().split())
import math
c_div = 0
d_div = 0
if a % c == 0:
    c_div = max(0, 1 + ((b - (b % c)) - a) // c )
else:
    c_div = max(0, 1 + ((b - (b % c)) - (a + (c - a % c))) // c )
if a % d == 0:
    d_div = max(0, 1 + ((b - (b % d)) - a) // d )
else:
    d_div = max(0, 1 + ((b - (b % d)) - (a + (d - a % d))) // d )
gcd_input = c * d // math.gcd(c, d)
if a % gcd_input == 0:
    c_d_div = max(0, 1 + ((b - (b % gcd_input)) - a) // gcd_input )
else: 
    c_d_div = max(0, 1 + ((b - (b % gcd_input)) - (a + (gcd_input - a % gcd_input))) // gcd_input )
print(b - a + 1 - d_div - c_div + c_d_div)