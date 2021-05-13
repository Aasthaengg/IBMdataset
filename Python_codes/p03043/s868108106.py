N, K = map(int, input().split())
sum = 0
for i in range(1, N+1):
	j = 0
	while True:
		if (i*(2**j)) >= K:
			break
		j += 1
	sum += (1/N)*((1/2)**j)
print(sum)