N = int(input())
S = input()

def solve(SS):
	n = len(SS)
	Z = [0] * n
	Z[0] = n
	i, j = 1, 0
	while i < n:
		while (i + j < n) and (SS[j] == SS[i + j]):
			j += 1
		Z[i] = j
		if j == 0:
			i += 1
			continue
		else:
			k = 1
			while (i + k < n) and (k + Z[k] < j):
				Z[i + k] = Z[k]
				k += 1
			i += k
			j -= k

	out = 0
	for i in range(n):
		tmp = min(Z[i], i)
		out = max(out, tmp)
	return out

ans = 0
for i in range(N):
	ans = max(ans, solve(S[i:]))

print(ans)