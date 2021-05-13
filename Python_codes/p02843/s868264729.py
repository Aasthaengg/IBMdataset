X = int(input())
dp = [False] * (X+1)
dp[0] = True
def judge(i, j):
    if i >= j:
        return dp[i-j]
    else:
        return False
    
for i in range(1, X+1):
    dp[i] = judge(i, 100) or judge(i, 101) or judge(i, 102) or judge(i, 103) or judge(i, 104) or judge(i, 105)
        
print(int(dp[X]))