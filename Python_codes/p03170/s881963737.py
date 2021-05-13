n,k = list(map(int, input().split()))
l = list(map(int, input().split()))
dp = [False]*(k+1)
for i in range(1,k+1):
    for e in l:
        if i-e>=0:
            if dp[i-e]==False:
                dp[i]=True
                break
if dp[k]:
    print("First")
else:
    print("Second")