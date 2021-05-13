N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    ans += LR[i][1] - LR[i][0] + 1
print(ans)