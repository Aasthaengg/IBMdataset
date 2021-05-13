def height(a, b, x, y, h):
	return h + abs(a - x) + abs(b - y)

n = int(input())
P = []
for i in range(n):
	x, y, h = map(int, input().split())
	P.append([x, y, h])

# sort by h
P.sort(key=lambda x: x[2], reverse=True)

for i in range(101):
	for j in range(101):
		H = height(i, j, P[0][0], P[0][1], P[0][2])
		for k in range(1, n):
			if max(H - abs(P[k][0] - i) - abs(P[k][1] - j), 0) != P[k][2]:
				break
		else:
			print(i, j, H)
			exit()