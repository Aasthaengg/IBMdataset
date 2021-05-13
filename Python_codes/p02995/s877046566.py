from math import gcd

a, b, c, d = map(int, input().split())
n = c * d // gcd(c,d)
x = (b // c) - ((a-1) // c)
y = (b // d) - ((a-1) // d)
z = (b // n) - ((a-1) // n)
print(b-a+1-(x+y-z))