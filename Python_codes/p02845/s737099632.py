import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
A = list(map(int, input().strip().split(" ")))
dp = {i: dict() for i in range(N)}
mod = 10 ** 9 + 7

def f(i, ma, mi):
    if i == N:
        return 1
    if (ma, mi) in dp[i]:
        return dp[i][(ma, mi)]
    if A[i] != ma and A[i] != mi and A[i] != i - ma - mi:
        dp[i][(ma, mi)] = 0
        return 0

    ans = 0
    # iがr, b, gを被って矛盾がないかを見ていく
    if A[i] == ma:
        ans += f(i + 1, ma + 1, mi)
    if A[i] == mi:
        if ma > mi + 1:
            ans += f(i + 1, ma, mi + 1)
        else:
            ans += f(i + 1, mi + 1, ma)
    if A[i] == i - ma - mi:
        ans += f(i + 1, ma, mi)

    dp[i][(ma, mi)] = ans % mod
    return ans % mod

print(f(0, 0, 0) % mod)