n = int(input())
ans = []
for i in range(1, n):
	for j in range(i, n + 1):
		if 2 * i!=i + j!=n + 1 - n % 2:
			ans.append("{} {}".format(i, j))
print(len(ans))
print("\n".join(ans))
