N = int(input())
MOD = 10 ** 9 + 7
D = [0] * 4
D[0] = 1

for i in range(N):
	ND = list(D)
	ND[0] = (D[0] * 8) % MOD
	ND[1] = (D[0] + D[1] * 9) % MOD
	ND[2] = (D[0] + D[2] * 9) % MOD
	ND[3] = (D[3] * 10 + D[1] + D[2]) % MOD
	D = ND

print(D[-1])
