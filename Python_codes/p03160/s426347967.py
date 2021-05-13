
n = int(input())
li = list(map(int,input().split()))

# dp = [[-1 for i in range(1100)] for j in range(1100)]
ans = [0]*n
ans[0] = 0
# def solve(a,b,dp,li):
#     if dp[a][b] !=-1 :
#         return dp[a][b]
#     else:
#         dp[a][b] = abs(li[a]-li[b])
#         return dp[a][b]

for i in range(2,n+1):
    if i == 2:
        ans[i-1]= abs(li[1]-li[0])
    else:
        ans[i-1] = min(abs(li[i-1]-li[i-2])+ans[i-2],abs(li[i-1]-li[i-3])+ans[i-3])

print(ans[-1])