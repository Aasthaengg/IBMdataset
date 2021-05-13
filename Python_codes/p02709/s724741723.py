# -*- coding: utf-8 -*-
import sys

N = int(input())
A = list(map(int,input().split()))

B = []
for i,a in enumerate(A):
    B.append([a,i])

B.sort(reverse = True)
#%%
def score(org_idx, sorted_idx):
    s,idx = B[org_idx]
    return s*abs(idx-sorted_idx)

dp = [[0]*(N+3) for _ in range(N+3)]
# dp[i][j] : 左からi個，右からj個詰めてある状態の時の最高スコア

for i in range(N+1):
    for j in range(N+1):
        if i+j == N:
            break
        idx = i+j
        dp[i+1][j] = max(dp[i+1][j], dp[i][j]+score(idx,i))
        dp[i][j+1] = max(dp[i][j+1], dp[i][j]+score(idx,N-j-1))
        # print('i,j={},{}'.format(i,j))
        # print(dp)
        
ans = 0
for i in range(N):
    ans = max(ans,dp[i][N-i])
print(ans)



