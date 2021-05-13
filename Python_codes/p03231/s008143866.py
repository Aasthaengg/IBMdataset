import math
import sys

def gcd(a,b):
	if b == 0:
		return a
	return gcd(b,a%b)


n,m = map(int, input().split())
s = input()
t = input()

if s[0] != t[0]:
	print(-1)
	sys.exit()

GCD = gcd(n,m)

if GCD == 1:
	print(n*m)
	sys.exit()

LCM = n*m//GCD


s_k = LCM//m
t_k = LCM//n
for i in range(GCD):
	if s[i*s_k] != t[i*t_k]:
		print(-1)
		sys.exit()

print(LCM)