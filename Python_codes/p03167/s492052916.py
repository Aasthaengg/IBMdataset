import numpy as np

H,W = map(int,input().split())
A = list()
for i in range(H):
    A.append(list(input()))
dp = [[0]*(W) for i in range(H)]
dp[0][0] = 1

for i in range(H):   
    for j in range(W):
        if A[i][j] == '.':
            # 横が行けるかどうか
            try:
                if A[i][j+1] == '.':
                    dp[i][j+1] += dp[i][j]
            except IndexError as e:
                # print('IndexError')
                pass
            # 縦が行けるかどうか
            try:
                if A[i+1][j] == '.':
                    dp[i+1][j] += dp[i][j]
        
            except IndexError as e:
                # print('IndexError')
                pass

print(dp[-1][-1] % (10**9 +7))
