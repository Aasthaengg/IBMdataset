H, W, D = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]
target = [[0,0] for _ in range(H*W+1)]
ruiseki = [[i+1] for i in range(D)]
ans = 0
for i in range(H):
    for j in range(W):
        target[grid[i][j]][0] = i+1
        target[grid[i][j]][1] = j+1
for i in range(D):
    tmp = ruiseki[i][0]
    ruiseki[i][0] = 0
    cnt = 0
    while tmp+D <= H*W:
        dist = abs(target[tmp][0]-target[tmp+D][0])+abs(target[tmp][1]-target[tmp+D][1])
        ruiseki[i].append(ruiseki[i][cnt]+dist)
        cnt += 1
        tmp += D
for i in range(Q):
    current = LR[i][0]
    tmp = D if current%D == 0 else current%D
    tmp -= 1
    print(ruiseki[tmp][((current-1)//D)+((LR[i][1]-current)//D)]-ruiseki[tmp][((current-1)//D)])