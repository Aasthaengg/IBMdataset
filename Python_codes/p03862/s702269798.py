N, x = map(int, input().split())
a = list(map(int, input().split()))

count = 0

for i, c in enumerate(a):
	try:
		j = a[i + 1]
	except IndexError:
		break
	while (a[i + 1] + c) > x:
		if (a[i + 1] + c) == x:
			break
		count += abs(x - (a[i + 1] + c))
		a[i + 1] -= abs(x - (a[i + 1] + c))
		if a[i + 1] <= 0:
			a[i + 1] = 0
			break
	else:
		continue

print(count)
