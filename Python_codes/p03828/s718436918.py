n = int(input())

mod = 10**9 + 7
d = {}

for i in range(2,n+1):
	x = i
	for j in range(2,x+1):
		while x % j == 0:
			x = x // j
			d[j] = d.get(j, 0) + 1

ret = 1
for v in d.values():
	ret *= v+1

print(ret % mod)
