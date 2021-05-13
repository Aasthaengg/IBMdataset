from math import gcd
from bisect import bisect_left, bisect_right

MOD = 10 ** 9 + 7
pow2 = [1] * (2 * 10 ** 5 + 1)
for i in range(1, 2 * 10 ** 5 + 1):
	pow2[i] = (pow2[i - 1] * 2) % MOD

N = int(input())
zero = 0
iwasies = []
for i in range(N):
	A, B = map(int, input().split())
	if A == 0 and B == 0:
		zero += 1
	elif A == 0:
		iwasies.append((0, 1))
	elif B == 0:
		iwasies.append((1, 0))
	else:
		g = gcd(A, B)
		A //= g
		B //= g
		if A < 0:
			iwasies.append((-A, -B))
		else:
			iwasies.append((A, B))

numiwasi = len(iwasies)
iwasies.sort()
badpairs = set()
for i in range(numiwasi):
	A, B = iwasies[i]
	abcount = bisect_right(iwasies, (A, B)) - bisect_left(iwasies, (A, B))
	
	Ao, Bo = B, -A
	if Ao < 0:
		Ao, Bo = -Ao, -Bo
	
	aobocount = bisect_right(iwasies, (Ao, Bo)) - bisect_left(iwasies, (Ao, Bo))
	
	if aobocount > 0:
		if (A, B) < (Ao, Bo):
			badpairs.add(((A, B, abcount), (Ao, Bo, aobocount)))
		else:
			badpairs.add(((Ao, Bo, aobocount), (A, B, abcount)))

sociable = numiwasi
ans = 1

for bp in badpairs:
	count1 = bp[0][2]
	count2 = bp[1][2]
	sociable -= (count1 + count2)
	ans = (ans * (pow2[count1] + pow2[count2] - 1)) % MOD
ans = (ans * pow2[sociable]) % MOD

print((ans + zero - 1) % MOD)	