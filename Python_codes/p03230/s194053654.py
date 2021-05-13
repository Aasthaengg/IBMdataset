import itertools
N = int(input())
for k in range(1000):
	if N * 2 == k * (k - 1):
		print("Yes")
		print(k)
		ans = [[] for i in range(k)]
		c = list(itertools.combinations(range(k), 2))
		for i in range(N):
			for j in c[i]:
				ans[j].append(i + 1)
		for i in ans:
			print(k - 1, end = " ")
			for j in i:
				print(j, end = " ")
			print()
		break
else:
	print("No")