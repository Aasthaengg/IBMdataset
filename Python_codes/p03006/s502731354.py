n = int(input())
ball = [list(map(int,input().split())) for i in range(n)]
ans = 0
for x in range(n):
    for y in range(n):
        if x == y:
            continue
        else:
            p = ball[x][0] - ball[y][0]
            q = ball[x][1] - ball[y][1]
            cou = 0
            for i in range(n):
                for j in range(n):
                    if ball[i][0]-ball[j][0] == p and ball[i][1]-ball[j][1] == q:
                        cou += 1
            ans = max(ans,cou)
print(n-ans)