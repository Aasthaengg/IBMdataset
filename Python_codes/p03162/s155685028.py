N=int(input())

nums=[]
for _ in range(N):
    nums.append(list(map(int, input().split())))

dp = [[0 for _ in range(3)] for _ in range(N)]


for i in range(N):
    a,b,c=nums[i]
    dp[i][0]=max(dp[i-1][1]+a,dp[i-1][2]+a)
    dp[i][1]=max(dp[i-1][0]+b,dp[i-1][2]+b)
    dp[i][2]=max(dp[i-1][0]+c,dp[i-1][1]+c)
num = max(dp[-1])
if N==1:
    num = max(nums[0])
print(num)
