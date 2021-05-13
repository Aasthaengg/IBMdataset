n, m = map(int, input().split())
L = [0] * n
for i in range(m):
	a, b = map(int, input().split())
	L[a - 1] += 1
	L[b - 1] += 1
print(*L, sep='\n')