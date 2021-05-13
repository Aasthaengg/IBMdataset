n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [False]*(k+1)
for j in range(1,k+1):
    tmp = False
    for i in range(n):
        if a[i] > j:
            continue
        if not dp[j-a[i]]:
            tmp = True
    dp[j] = tmp

if dp[-1]:
    print("First")
else:
    print("Second")