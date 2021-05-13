import sys
sys.setrecursionlimit(10 ** 6)
n , m = map(int,input().split())
coins = list(map(int,input().split()))
coins.sort(reverse=True)
dp = [[float("inf")]*(n + 1) for _ in range(m + 1)]
def solve(i , value):
    if dp[i][value] != float("inf"):
        return dp[i][value]
    if i == m - 1 or value == 0:
        ret_val = value
    elif coins[i] > value:
        ret_val = solve(i + 1,value)
    else:
        ret_val = min(solve(i + 1,value) , solve(i,value - coins[i]) + 1)
    dp[i][value] = ret_val
    return ret_val

solve(0 , n)
print(dp[0][n])
