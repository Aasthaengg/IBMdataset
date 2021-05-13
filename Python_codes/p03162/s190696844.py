
#B- Frog 2

def solution(nums):
    n = len(nums)
    dp = [0,0,0]
    for day in range(n):
        new_dp = [0,0,0]
        for i in range(3):
            for j in range(3):
                if i!=j:
                    new_dp[i] = max(new_dp[i] , dp[j]+ nums[day][i] )
        dp = new_dp
    return max(dp[0],dp[1],dp[2])

N = int(input())
nums = []
for _ in range(N):    
    day = list(map(int,input().split()))
    nums.append(day)
res = solution(nums)
print(res)
