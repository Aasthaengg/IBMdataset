def main():
	t = input().split(" ")
	n, m, d = int(t[0]), int(t[1]), int(t[2])
	if d == 0:
		r = (m-1) / n
	elif d > n:
		r = 0
	else:
		r = 2 * (n-d) * (m-1) / n / n
	print(r)
main()
