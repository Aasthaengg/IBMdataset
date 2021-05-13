def canusol(n, m, c, a, b):
	count = 0
	ans = 0
	for i in range(n):
		count = 0
		for j in range(m):
			count += a[i][j] * b[j]
		if count + c > 0:
			ans += 1
	return ans
n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = []
for _ in range(n):
	l = list(map(int, input().split()))
	a.append(l)
print(canusol(n, m, c, a, b))