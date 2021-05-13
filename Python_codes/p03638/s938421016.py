H, W = map(int,input().split())
N = int(input())
a = list(map(int,input().split()))
b =[0]*(H*W)
k = 0
for i in range(N):
    for j in range(a[i]):
        b[k] = i + 1
        k += 1
x, y = 0, 0
ans =[[0]*W for i in range(H)]
for i in range(H*W):
    ans[y][x] = b[i]
    if (x == 0 and y%2 == 1) or (x == W - 1 and y%2 == 0):
        y += 1
    elif y%2 == 0:
        x += 1
    else:
        x -= 1
for _ in range(H):
    print(*ans[_])