n = int(raw_input())
f = []
for i in range(10):
	f.append([0 for _ in range(10)])
ans = 0

for a in range(1, n + 1):
	val = a
	first, last = 0, val % 10
	while val != 0:
		first = val % 10
		val = val / 10
	f[first][last] += 1

for a in range(1, n + 1):
	val = a
	first, last = 0, val % 10
	while val != 0:
		first = val % 10
		val = val / 10
	ans += f[last][first]

print ans