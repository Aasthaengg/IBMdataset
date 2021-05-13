MOD = 10**9 + 7
S = input()
res = 0
dpn = 1
dp0 = 0 # a
dp1 = 0 # ab

for c in S:
    if c == 'A':
        dp0 += dpn
    elif c == 'B':
        dp1 += dp0
    elif c == 'C':
        res += dp1
    else:
        dp0,dp1,res = dp0*3+dpn,dp1*3+dp0,res*3+dp1
        dpn *= 3
    dpn %= MOD
    dp0 %= MOD
    dp1 %= MOD
    res %= MOD
print(res)
