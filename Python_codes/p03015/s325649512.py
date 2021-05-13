MOD = 10**9+7
L = input().rstrip()
res = 1
cnt = 0
for s in L:
    res *= 3
    if s=="0":
        res -= pow(2,cnt+1,MOD)
    else:
        cnt += 1
    res %= MOD
print(res)