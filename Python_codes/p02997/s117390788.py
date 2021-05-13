def s():
	n, k = map(int, input().split())
	ans = ["1 {}".format(i) for i in range(2, n + 1)]
	c = (n - 1) * (n - 2) // 2
	if k > c:
		print(-1)
		exit()
	for i in range(2, n):
		for j in range(i + 1, n + 1):
			if c == k:
				break
			ans += ["{} {}".format(i, j)]
			c -= 1
		else:
			continue
		break
	print(len(ans))
	print(*ans)

if __name__=="__main__":
	s()