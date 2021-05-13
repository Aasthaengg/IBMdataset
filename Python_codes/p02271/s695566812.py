import sys
def input():
    return sys.stdin.readline()[:-1]

n  = int(input())
A = list(map(int, input().split()))
q  = int(input())
M = list(map(int, input().split()))

def solve(dp, n,A, i,m):
    if m==0:
        return True
    
    elif i>=n:
        return False
    
    elif dp[i][m] is not None:
        return dp[i][m]
    
    elif solve(dp,n,A, i+1,m):
        dp[i][m] = True
        return True
    
    elif m-A[i]>=0:
        dp[i][m] = solve(dp,n,A, i+1,m-A[i])
        return dp[i][m]
    
    else:
        dp[i][m]= False
        return False
    

dp = [[None for i in range(max(M)+1)] for j in range(n+1)]

for m in M:    
    if solve(dp, n,A, 0, m):
        print('yes')
    else:
        print('no')
