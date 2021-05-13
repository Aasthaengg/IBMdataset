import sys
sys.setrecursionlimit(10**7)
MOD = 10**9+7
l = [int(i) for i in sys.stdin.readline().strip()]
#i番目までで決まってない時
dp0 = [0] * (len(l) + 1)
#i番目までで決まっている時
dp1 = [0] * (len(l) + 1)
dp0[0] = 1
for i, _l in enumerate(l, 1):
    if _l == 0:
        dp0[i] = dp0[i-1]
        dp1[i] = dp1[i-1] * 3
    else:
        dp0[i] = dp0[i-1] * 2
        dp1[i] = dp1[i-1] * 3 + dp0[i-1]
    dp0[i] %= MOD
    dp1[i] %= MOD
res = dp0[-1] + dp1[-1]
res %= MOD
print(res)