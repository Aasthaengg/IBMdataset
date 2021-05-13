d = {"Male" : 1, "Female" : 2, "Vacant" : 0}

def check(l, r, a, b):
	if (a != b):
		return ((r - l + 1) % 2 == 1)
	else:
		return ((r - l + 1) % 2 == 0)

def get(k):
	print(k - 1)
	return d[input()]

def main():
	n = int(input())
	left = get(1)
	if (left == 0): return
	right = get(n)
	if (right == 0): return

	l, r = 1, n
	while (l + 2 < r):
		m = (l + r) // 2
		med = get(m)
		if (med == 0): return
		if (check(l, m, left, med)):
			right, r = med, m
		else:
			left, l = med, m
	get(l + 1)

main()