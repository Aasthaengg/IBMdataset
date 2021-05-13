MOD = 10 ** 9 + 7
N = int(input())
S1 = input()
S2 = input()

ans = 1
prv_ptn = 0 # 1 or 2
i = 0
while i < N:
    if S1[i] == S2[i]:
        if prv_ptn == 0:
            ans *= 3
        elif prv_ptn == 1:
            ans *= 2
        else:
            ans *= 1
        ans %= MOD
        prv_ptn = 1
        i += 1
    else:
        if prv_ptn == 0:
            ans *= 6
        elif prv_ptn == 1:
            ans *= 2
        else:
            ans *= 3
        ans %= MOD
        prv_ptn = 2
        i += 2
print(ans % MOD)
