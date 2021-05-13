n,k = map(int,input().split())
al = list(map(int,input().split()))

dp = [0 for i in range(k+1)]

for i in range(k+1):
    for a in al:
        if a <= i:
            if dp[i-a] == 0:
                dp[i] = 1


if dp[-1] % 2 == 0:
    print("Second")
else:
    print("First")

