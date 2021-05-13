n,k = map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
dp=[-1]*(k+1)

for i in range(1,k+1):
    m=1
    for j in arr:
        if(i>=j):
            m = min(dp[i-j],m)
    dp[i] = -1*m

if(dp[k]==1):
    print("First")
else:
    print("Second")