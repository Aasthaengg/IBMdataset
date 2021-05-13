H,W = map(int,(input().split()))
N = int(input())
a = list(map(int,(input().split())))
b = [[0]*W for _ in range(H)]
nowx,nowy = 0,0
nowc = 0
for i in range(H*W):
    b[nowx][nowy] = nowc +1
    a[nowc] -= 1
    if a[nowc] == 0:
        nowc += 1
    if nowy %2 == 0:
        if nowx + 1 >= H:
            nowy += 1
        else:
            nowx += 1
    else:
        if nowx - 1 < 0:
            nowy += 1
        else:
            nowx -= 1

for i in range(H):
    print(*b[i])