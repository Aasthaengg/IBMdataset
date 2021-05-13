from collections import defaultdict
s = input()
lens = len(s)
"""
1, 10, 100～900に対して13で割って5余るものは存在する？
"""
modl = [[] for i in range(len(s))]
modl[0] = [i for i in range(10)]
for i in range(1, len(s)):
	modl[i] = [(modl[i-1][j]*10)%13 for j in range(10)]
mod = 10**9+7

unta = defaultdict(lambda: 0)
unta[0] += 1
for i, j in enumerate(s[::-1]):
	newunta = defaultdict(lambda: 0)
	if j != "?":
		a = modl[i][int(j)]
		for k in range(13):
			newunta[(k+a)%13] = (newunta[(k+a)%13] + unta[k]) % mod
	else:
		for l in range(10):
			a = modl[i][l]
			for k in range(13):
				newunta[(k+a)%13] = (newunta[(k+a)%13] + unta[k]) % mod
	unta = newunta

print(unta[5] % mod)