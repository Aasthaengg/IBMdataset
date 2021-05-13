H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))

ans = [[0] * W for _ in range(H)]
k = 0
for i in range(H):
    for j in range(W):
        if i % 2 == 0:
            ans[i][j] = k+1
        else:
            ans[i][W-1-j] = k+1
        a[k] -= 1
        if a[k] == 0:
            k += 1
for i in range(H):
    print(' '.join(map(str, ans[i])))
