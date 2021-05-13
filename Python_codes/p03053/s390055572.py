import sys
input = sys.stdin.readline

H, W = map(int, input().split())
G = [[i for i in input()] for j in range(H)]

ls = []
dp = [[-1 for i in range(W)] for j in range(H)]
for h in range(H):
    for w in range(W):
        if G[h][w] == "#":
            ls.append([h,w])
            dp[h][w] = 1

ans = -1
while len(ls) > 0:
    ans += 1
    temp = []
    for h, w in ls:
        if 0 <= h+1 <= H-1 and dp[h+1][w] == -1:
            dp[h+1][w] = 1
            temp.append([h+1,w])
        if 0 <= h-1 <= H-1 and dp[h-1][w] == -1:
            dp[h-1][w] = 1
            temp.append([h-1,w])
        if 0 <= w+1 <= W-1 and dp[h][w+1] == -1:
            dp[h][w+1] = 1
            temp.append([h,w+1])
        if 0 <= w-1 <= W-1 and dp[h][w-1] == -1:
            dp[h][w-1] = 1
            temp.append([h,w-1])
    ls = temp

print(ans)