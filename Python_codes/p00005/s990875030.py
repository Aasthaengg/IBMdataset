import sys
import fractions as f
for l in sys.stdin.readlines():
	a,b=map(int,l.split())
	print f.gcd(a,b),a*b/f.gcd(a,b)