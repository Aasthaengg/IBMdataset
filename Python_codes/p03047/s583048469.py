N, K = [int(x) for x in input().split()]

x = [i for i in range(1, N+1)]

summ = 0

for i, n in enumerate(x):
	if i + K <= len(x):
		summ=summ+1

print(summ)