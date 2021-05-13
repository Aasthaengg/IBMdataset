L = input()

dp1 = [0 for i in range(len(L))]
dp2 = [0 for i in range(len(L))]

dp1[0] = 2
dp2[0] = 1

mod = 10 ** 9 + 7

for i in range(1,len(L)):
    if L[i] == "0":
        dp1[i] = dp1[i-1]
    else:
        dp1[i] = dp1[i-1] * 2
        dp2[i] = dp1[i-1]
    dp2[i] += dp2[i-1] * 3
    dp1[i] %= mod
    dp2[i] %= mod

print((dp1[len(L)-1] + dp2[len(L)-1]) % mod)