import collections
N = int(input())
A = [int(_) for _ in input().split()]
dp = collections.defaultdict(int)
dp[0] = 1
ans = 0
for a in A:
    dp_new = collections.defaultdict(int)
    dp_new[0] = 1
    for b in dp:
        if a & b == 0:
            dp_new[a + b] += dp[b]
            ans += dp[b]
    dp = dp_new
print(ans)
