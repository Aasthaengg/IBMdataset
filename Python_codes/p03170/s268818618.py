n, k = map(int, input().split())
a = [int(x) for x in input().split()]

dp = [-1 for _ in range(k+1)]

for i in range(min(a)):
    dp[i] = 1

for i in range(k+1):
    tmp = 0
    for x in a:
        if i-x < 0:
            continue
        else:
            tmp += dp[i-x]
    if tmp > 0:
        dp[i] = 0
    else:
        dp[i] = 1

print('First' if dp[k] == 0 else 'Second')
