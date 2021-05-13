l = input()
mod = 10**9 + 7
#上からi桁目まで決めて、まだl以下であることが確定していない
dp1 = [0 for i in range(len(l))]
dp1[0] = 2
#上からi桁目まで決めて、もうl以下であることが確定してる
dp2 = [0 for i in range(len(l))]
dp2[0] = 1
for i in range(1,len(l)):
    if l[i] == "0":
        #今回の桁を0にする
        dp1[i] += dp1[i-1]
        dp2[i] += dp2[i-1]
        #今回の桁を1にする
        dp2[i] += dp2[i-1] * 2
    else:
        #今回の桁を0にする
        dp2[i] += dp2[i-1] + dp1[i-1]
        #今回の桁を1にする
        dp1[i] += dp1[i-1] * 2
        dp2[i] += dp2[i-1] * 2
    dp1[i] %= mod
    dp2[i] %= mod
print((dp2[-1] + dp1[-1]) % mod)