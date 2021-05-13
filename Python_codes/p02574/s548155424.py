from math import gcd

N = int(input())
A = list(map(int, input().split()))

v = 0
for a in A: v = gcd(a, v)
if v > 1:
	print('not coprime')
	raise SystemExit


V = set()
for v in A:
	for i in range(2, v+1):
		if i * i > v: break
		if v % i == 0:
			if v in V:
				print('setwise coprime')
				raise SystemExit

			V.add(v)
			while v % i == 0: v //= i
	if v != 1:
		if v in V:
			print('setwise coprime')
			raise SystemExit

		V.add(v)

print('pairwise coprime')
