N, A, B = map(int, input().split())

total = 0
for i in range(1, N + 1):
	res = sum(list(map(int, str(i))))
	if A <= res <= B:
		total += i
print(total)
