n, k = map(int, input().split())
l = [0] * (10000001)
for _ in range(n):
	a, b = map(int, input().split())
	l[a] += b
for i in range(1, 10000001):
	if k <= l[i]:
		print(i)
		break
	k -= l[i]