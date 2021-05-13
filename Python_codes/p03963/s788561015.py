n, k = map(int, input().split())
v = 0
for i in range(n):
	if i == 0:
		v = k
	else:
		v = v*(k-1)
print(v)