N, P = map(int, input().split())
As = list(map(int, input().split()))

MOD = 2 ** 61 - 1
table_len = 100

fac = [1, 1]
for i in range(2, table_len):
    fac.append(fac[-1] * i % MOD)

finv = [0] * table_len
finv[-1] = pow(fac[-1], MOD - 2, MOD)
for i in range(table_len-1, 0, -1):
    finv[i-1] = finv[i] * i % MOD

C = 0
D = 0
for A in As:
    if A % 2:
        D += 1
    else:
        C += 1

ans = pow(2, C)
ans *= sum( ((fac[D] * finv[i] * finv[D-i])%MOD for i in range(P, D+1, 2)) )
print(ans)