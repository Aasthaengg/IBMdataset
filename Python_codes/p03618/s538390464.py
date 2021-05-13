a = input()
n = len(a)
ans = n * (n - 1) // 2 + 1
d = {}
for x in a:
	d[x] = d.get(x, 0) + 1
print(ans - sum(y * (y - 1) // 2 for y in d.values()))