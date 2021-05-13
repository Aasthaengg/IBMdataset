h,w = map(int,input().split())
s = ["" for i in range(h)]
for i in range(h):
    s[i] = input()

def pl(x1,y1,x2,y2):
    if s[x1][y1] == "." and s[x2][y2] == "#":
        return 1
    else:
        return 0

dp = [[0 for i in range(w)] for j in range(h)]
for i in range(h):
    for j in range(w):
        if i == 0 and j == 0 and s[i][j] == "#":
            dp[i][j] += 1
        elif i == 0:
            dp[i][j] = dp[i][j-1]+pl(i,j-1,i,j)
        elif j == 0:
            dp[i][j] = dp[i-1][j]+pl(i-1,j,i,j)
        else:
            dp[i][j] = min(dp[i][j-1]+pl(i,j-1,i,j),dp[i-1][j]+pl(i-1,j,i,j))

print(dp[h-1][w-1])
