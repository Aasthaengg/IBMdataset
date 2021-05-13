N = int(input())
As = list(map(int, input().split()))

from math import gcd
g = 0
for a in As:
	g = gcd(g, a)
print(g)