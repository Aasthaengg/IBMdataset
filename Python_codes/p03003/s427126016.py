inpl = lambda: list(map(int,input().split()))
MOD = 10**9 + 7
N, M = inpl()
S = inpl()
T = inpl()

total = [0]*(N+1)*(M+1)
for i in range(N):
	for j in range(M):
		if S[i] == T[j]:
			n = total[(M+1)*i+j] + 1
		else:
			n = 0
		total[(M+1)*(i+1)+(j+1)] = (n + total[(M+1)*i+(j+1)] + total[(M+1)*(i+1)+j] - total[(M+1)*i+j]) % MOD
print((total[-1]+1) % MOD)