def getlist():
	return list(map(int, input().split()))

N, M = getlist()
S = getlist()
T = getlist()

L = [[1 for i in range(N + 1)] for j in range(M + 1)]
for i in range(1, N + 1):
	for j in range(1, M + 1):
		if S[i - 1] == T[j - 1]:
			L[j][i] = (L[j - 1][i] + L[j][i - 1]) % 1000000007
		else:
			L[j][i] = (L[j - 1][i] + L[j][i - 1] - L[j - 1][i - 1]) % 1000000007

print(L[M][N] % 1000000007)