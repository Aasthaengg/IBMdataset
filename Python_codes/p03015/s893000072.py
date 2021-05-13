L = input()

mod = 10 ** 9 + 7
n = len(L)
dp1 = 0
dp2 = 0

for i in range(n):
    if L[i] == "1":
        dp1 = (dp1 + pow(2, dp2, mod) * pow(3, n-i-1, mod)) % mod
        dp2 = dp2 + 1

dp1 = (dp1 + pow(2, dp2, mod)) % mod
print(dp1)
