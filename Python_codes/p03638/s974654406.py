H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))
ans = [[0] * W for i in range(H)]
pre = 0
cur = 1
for i in range(H):
    if i % 2 == 0:
        cnt = 0
        while cnt < W:
            if a[cur - 1] == 0:
                cur += 1
            ans[i][cnt] = cur
            a[cur - 1] -= 1
            cnt += 1
        #print(ans)
    else:
        cnt = W - 1
        while cnt >= 0:
            if a[cur - 1] == 0:
                cur += 1
            ans[i][cnt] = cur
            a[cur - 1] -= 1
            cnt -= 1
        #print(ans)
for i in range(H):
    print(*ans[i])
