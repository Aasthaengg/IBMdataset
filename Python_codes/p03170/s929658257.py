n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
dp = [False] * (k + 1)
for i in range(1, k + 1):
    ok = False
    for j in a:
        if i - j >= 0:
            ok = ok or (not dp[i - j])
    dp[i] = ok

if dp[-1]:
    print("First")
else:
    print("Second")
