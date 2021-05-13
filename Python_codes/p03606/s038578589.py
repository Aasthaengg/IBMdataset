N = int(input())
LR = [list(map(int,input().split())) for i in range(N)]
cnt = 0
for i in range(N):
    for j in range(1):
        cnt += LR[i][j+1] - LR[i][j] +1
print(cnt)