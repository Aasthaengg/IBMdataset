"""
全ての桁でa, b共に0ではない場合を考えれば良い。
"""
mod = 10 ** 9 + 7
L = input()

dp1 = 0
dp2 = 1

for l in L:
    if l == "1":
        dp1 = dp1 * 3 + dp2
        dp2 = dp2 * 2

    else:
        dp1 = dp1 * 3
    dp2 %= mod
    dp1 %= mod

print((dp1 + dp2) % mod)
