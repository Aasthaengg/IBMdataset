n, k = map(int, input().split())

a = list(map(int, input().split()))

dp = [''] * (k + 1)

for i in range(a[0]):
    dp[i] = 'Second'

for x in a:
    dp[x] = 'First'

for i in range(1, k + 1):
    if dp[i] != '':
        continue

    dp[i] = 'Second'
    for x in a:
        if x > i:
            continue
        if dp[i-x] == 'Second':
            dp[i] = 'First'
            break

print(dp[-1])
