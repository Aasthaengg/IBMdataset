n, h, w = map(int, input().split())
ab = [input().split() for _ in range(n)]
c = 0

for i in range(n):
	if int(ab[i][0]) >= h and int(ab[i][1]) >= w:
		c += 1

print(c)