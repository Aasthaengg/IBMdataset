S = input()
T = input()
N, M = len(S), len(T)
ans = 1000
for i in range(N - M + 1):
	sub = S[i:i + N]
	temp = 0
	for j in range(M):
		if sub[j] != T[j]:
			temp += 1
	if (temp < ans):
		ans = temp
print(ans)