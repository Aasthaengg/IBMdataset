S, T = [input() for _ in range(2)]
answer = 1001

for i in range(len(S) - len(T) + 1):
	k = 0
	U = S[i:i + len(T)]
	for j in range(len(T)):
		if T[j] != U[j]:
			k += 1
	answer = min(answer, k)
print(answer)