ll = list(input())

dp1 = [0 for i in range(len(ll))]
dp2 = [0 for i in range(len(ll))]
for idx, l in enumerate(ll):
    if l == "1":
        if idx == 0:
            dp1[0] = 2
            dp2[0] = 1
        else:
            dp1[idx] = dp1[idx-1] * 2
            dp2[idx] = dp2[idx-1] * 3 + dp1[idx-1]
            dp1[idx] %= 10**9+7
            dp2[idx] %= 10**9+7
    else:
        dp1[idx] = dp1[idx-1]
        dp2[idx] = dp2[idx-1] * 3
        dp2[idx] %= 10**9+7

print((dp1[-1] + dp2[-1]) % (10**9+7))