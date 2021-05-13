def lucas_dp(n):
    memo = [None] * (n + 1)
    memo[0] = 2
    memo[1] = 1
    for i in range(2, n+1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]  

n = int(input())
lucas = lucas_dp(n)
print(lucas)
