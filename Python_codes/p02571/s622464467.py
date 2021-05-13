S, T = [input() for _ in range(2)]

answer = float("inf")

for i in range(len(S) - len(T) + 1):
	k = 0
	S_subset = S[i:i + len(T)]
	for t, s in zip(T, S_subset):
		if t != s:
			k += 1
	answer = min(answer, k)
print(answer)