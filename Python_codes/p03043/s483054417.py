import math

N, K = map(int, input().split())
probability = 0

for n in range(1, N + 1):
	if n < K:
		p = math.ceil((math.log2(K / n )))
		probability = probability + 1/((2**p)*N)
	else:
		probability = probability + 1 / N

print(probability)