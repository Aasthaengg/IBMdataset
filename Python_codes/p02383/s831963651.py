a = list(map(int, input().split()))
for d in input():
	b = []
	if d == "N":
		b = [a[1], a[5], a[2], a[3], a[0], a[4]]
	elif d == "E":
		b = [a[3], a[1], a[0], a[5], a[4], a[2]]
	elif d == "S":
		b = [a[4], a[0], a[2], a[3], a[5], a[1]]
	else:
		b = [a[2], a[1], a[5], a[0], a[4], a[3]]
	a = b
print(a[0])

