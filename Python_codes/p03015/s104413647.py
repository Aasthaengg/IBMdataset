L = list(map(int,list(input())))
num = len(L)
mod = 10 ** 9 + 7

dp1 = [0] * num
#AおよびBの値の上からk桁目(k>=0)までを確定させ、その時点で
#既にA+BがL以下であることが分かっているような値組(A, B)の個数
dp2 = [0] * num
#AおよびBの値の上からk桁目(k>=0)までを確定させ、その時点では
#まだA+BがL以下になるかどうか分かっていないような値組 (A, B) の個数

dp1[0] = 1 #(A,B)=(0,0)
dp2[0] = 2 #(A,B)=(1,0),(0,1)

for i in range(1,num):
    if L[i] == 1:
        dp1[i] = dp1[i-1] * 3 + dp2[i-1]
        dp2[i] = dp2[i-1] * 2
    else:
        dp1[i] = dp1[i-1] * 3
        dp2[i] = dp2[i-1]
    dp1[i] %= mod
    dp2[i] %= mod

print((dp1[num-1] + dp2[num-1])%mod)