n = int(input())

sum = (n // 2) * 2 + 1

ans = []

for i in range(1, n + 1):
	for j in range(i + 1, n + 1):
		if i + j != sum:
			ans.append([i, j])
print(len(ans))

for i in ans:
	print(i[0], i[1])
