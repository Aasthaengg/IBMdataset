import sys
sys.setrecursionlimit(10**7)

h,w = map(int,input().split())
sij = [input() for i in range(h)]

dp = [[10**18 for i in range(w)] for j in range(h)]

dp[0][0] = 0

for i in range(w-1):
    if sij[0][i+1] != sij[0][i]:
        dp[0][i+1] = dp[0][i]+1
    else:
        dp[0][i+1] = dp[0][i]
        
for i in range(h-1):
    if sij[i+1][0] != sij[i][0]:
        dp[i+1][0] = dp[i][0]+1
    else:
        dp[i+1][0] = dp[i][0]

for i in range(1,h):
    for j in range(1,w):
        #print(i,j)
        if sij[i-1][j] != sij[i][j]:
            sita = dp[i-1][j]+1
        else:
            sita = dp[i-1][j]
        if sij[i][j-1] != sij[i][j]:
            yoko = dp[i][j-1]+1
        else:
            yoko = dp[i][j-1]
        #print(i,j,sita,yoko)
        dp[i][j] = min(sita,yoko)

add = 0
#print(dp)

if sij[0][0] == '#':
    add = 1
"""
if dp[h-1][w-1] == 1:
    print(1)
else:
    print(dp[h-1][w-1]//2+add)
""" 
if dp[h-1][w-1] % 2 == 1:
    print(dp[h-1][w-1]//2+1)
else:
    print(dp[h-1][w-1]//2+add)