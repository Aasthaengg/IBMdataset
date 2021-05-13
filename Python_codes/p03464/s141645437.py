def main():
	k, *a = map(int, open(0).read().split())
	m = M = 2
	for x in a[::-1]:
		M -= M % x
		if m > M:
			print(-1)
			exit()
		m += -m % x
		M += x - 1
	print(m, M)

if __name__=="__main__":
	main()
