n, k = map(int, input().split())
MOD = 10 ** 9 + 7
for i in range(1, k+1):
    if i == 1:
        comb1 = n - k + 1
        comb2 = 1
    else:
        comb1 *= (n - k + 2 - i) * pow(i, MOD-2, MOD)
        comb2 *= (k - i + 1) * pow(i - 1, MOD-2, MOD)
    print(comb1 * comb2 % MOD)
