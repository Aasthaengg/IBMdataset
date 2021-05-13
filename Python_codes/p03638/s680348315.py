h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

i = 0

for y in range(h):
	grid = []
	for x in range(w):
		grid.append(i + 1)
		a[i] -= 1
		if a[i] == 0:
			i += 1
	
	if y % 2 == 0:
		print(*grid)
	else:
		print(*grid[::-1])

