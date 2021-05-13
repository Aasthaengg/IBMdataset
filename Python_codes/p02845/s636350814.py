MOD = 10**9 + 7
def solve(n, a):
    dp = [3] + [0] * n
    res = 1
    for x in a:
        res = res * dp[x] % MOD
        if res == 0:
            break
        dp[x] -= 1
        dp[x+1] += 1
    return res

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))