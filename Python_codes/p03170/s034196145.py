n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [False]*(k+1)

for i in range(k+1):
    flag = 0
    for j in a:
        if i-j < 0:
            continue
        if not dp[i-j]:
            flag = 1
            break

    if flag:
        dp[i] = True

if dp[k]:
    print("First")
else:
    print("Second")
