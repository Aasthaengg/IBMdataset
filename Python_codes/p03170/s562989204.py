n, k = map(int, input().split())
a = list(map(int, input().split()))
#dp[i] - TRUE if the first player wins if there are i stones remaining
dp = [False] * (k + 1)
for stones in range(k + 1):
    for x in a:
        if stones >= x and not dp[stones - x]:
            dp[stones] = True
print('First' if dp[k] else 'Second')