n, k = map(int, input().split())
comb = [[1 if (i >= j) else 0 for j in range(n+1)] for i in range(n+1)]

MOD = 10 ** 9 + 7

for i in range(1, n+1):
    for j in range(1, i):
        comb[i][j] = (comb[i-1][j] + comb[i-1][j-1]) % MOD


for i in range(1,k+1):
    print(comb[n-k+1][i] * comb[k-1][i-1] % MOD)

