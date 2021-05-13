import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
L = 50
dp = [[-float('inf')]*2 for _ in range(L+1)]
dp[0][0] = 0

for i in range(L):
    Ki = (K>>(L-1-i))&1
    
    for j in range(2):
        for k in range(2 if j else Ki+1):
            add = 0
            
            for Ai in A:
                add += k^((Ai>>(L-1-i))&1)
            
            dp[i+1][j|(k<Ki)] = max(dp[i+1][j|(k<Ki)], dp[i][j]+add*2**(L-1-i))
            
print(max(dp[L]))