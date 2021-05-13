L = input()

mod = 10 ** 9 + 7
n = len(L)
dp1 = 1
dp2 = 0

for i in range(n):
    if L[i] == "0":
        dp2 = (dp2 * 3) % mod
    else:
        dp2 = (dp1 + dp2 * 3) % mod
        dp1 = (dp1 * 2) % mod

print((dp1 + dp2) % mod)
