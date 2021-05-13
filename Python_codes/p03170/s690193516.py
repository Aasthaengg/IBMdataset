n,k = map(int,input().split())
arr = list(map(int,input().split()))

dp = [False]*(k+1)

for stones in range(k+1):
    for x in arr:
        if stones >= x and dp[stones-x] == False:
            dp[stones] = True

if dp[k]:
    print("First")
else:
    print("Second")
