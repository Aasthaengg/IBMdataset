N, A, B = map(int, input().split())
X = list(map(int, input().split()))

sum_cost = 0
for n in range(1, N):
	cost = (X[n] - X[n - 1]) * A
	if B < cost:
		sum_cost += B
	else:
		sum_cost += cost
	#print(sum_cost)
print(sum_cost)
