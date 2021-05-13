# dp[i] - True if first player has i stones and win

n, k = [int(x) for x in input().split()]

arr = [int(x) for x in input().split()]

dp = [False for _ in range(k+1)]

for i in range(k+1):
    for x in arr:
        if i-x >= 0 and not dp[i-x]:
            dp[i] = True

print("First" if dp[k] else "Second")
