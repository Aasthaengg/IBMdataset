NUM = (None, 2, 5, 5, 4, 5, 6, 3, 7, 6)

nSticks, n = map(int, input().split())
a = list(map(int, input().split()))

# maximum value to make using exactly sticks
dp = [0] * (nSticks + 1)
for digit in a:
    if NUM[digit] <= nSticks:
        dp[NUM[digit]] = max(dp[NUM[digit]], digit)
for sticks in range(2, nSticks + 1):
    for digit in a:
        if sticks - NUM[digit] >= 0 and dp[sticks - NUM[digit]] > 0:
            dp[sticks] = max(dp[sticks], dp[sticks - NUM[digit]] * 10 + digit)
print(dp[-1])

