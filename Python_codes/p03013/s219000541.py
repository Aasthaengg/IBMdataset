def solve():
    for i in range(2, n+1):
        prev1 = dp[i-1]
        prev2 = dp[i-2]
        if i in set:
            continue
        else:
            dp[i] = prev1 + prev2
    return dp[n]


n, m = map(int, input().split())
lst = []
for i in range(m):
    lst.append(int(input()))
set = set(lst)
dp = [0] * (n+1)
dp[0] = 1
if 1 not in set:
    dp[1] = 1
res = solve()
print(res%1000000007)