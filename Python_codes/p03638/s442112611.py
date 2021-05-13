H,W = map(int,input().split())
N = int(input())
a = list(map(int,input().split()))

ans = [[0]*W for i in range(H)]
now = 1
cnt = 0
for i in range(H):
    if i&1:
        for j in reversed(range(W)):
            if cnt == a[now-1]:
                now += 1
                cnt = 0
            ans[i][j] = now
            cnt += 1

    else:
        for j in range(W):
            if cnt == a[now-1]:
                now += 1
                cnt = 0
            ans[i][j] = now
            cnt += 1

for i in range(H):
    print(*ans[i])