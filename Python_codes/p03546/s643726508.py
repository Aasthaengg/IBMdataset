H,W = map(int,input().split())
costMap = [list(map(int,input().split())) for _ in range(10)]
wall = [list(map(int,input().split())) for _ in range(H)]

memo = [float("INF")]*(10)
memo[1] = 0
flag = True
while flag:
    flag = False
    for i in range(10):
        for j in range(10):
            if memo[i]+costMap[j][i] < memo[j]:
                memo[j] = memo[i]+costMap[j][i]
                flag = True
ans = 0
for i in range(H):
    for j in range(W):
        a = wall[i][j]
        if a != -1:
            ans += memo[a]
print(ans)