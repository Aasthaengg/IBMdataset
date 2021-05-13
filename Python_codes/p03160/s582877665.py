

def solution(h):
    n = len(h)
    INF = float('inf')
    dp = [INF]*n
    dp[0] = 0
    for i in range(n):
        for j in range(i+1,i+3):
            if j < n:
                dp[j] = min(dp[j] , dp[i]+abs(h[i]-h[j]) )
    
    return dp[n-1]

N = int(input())
h = list(map(int,input().split()))
res = solution(h)
print(res)
