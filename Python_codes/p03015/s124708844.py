L = input()
MOD = 10**9+7

num_ab = [1]
for i in range(1, len(L)+1):
    num_ab.append((num_ab[-1] * 3) % MOD)

ans, m = 0, 1
while True:
    if '0' not in L:
        ans = (ans + (m * num_ab[len(L)]) % MOD) % MOD
        print(ans)
        exit()
    elif '1' not in L[1:]:
        ans = (ans + ((m * num_ab[len(L) - 1]) % MOD + (2 * m) % MOD) % MOD) % MOD
        print(ans)
        exit()
    else:
        ans = (ans + (m * num_ab[len(L) - 1]) % MOD) % MOD
        L = L[L[1:].index('1') + 1:]
        m = (2 * m) % MOD