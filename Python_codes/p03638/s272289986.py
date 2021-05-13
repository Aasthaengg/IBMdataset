H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))
ans = [list([0] * W) for _ in range(H)]

color = 1
for i in range(H):
    for j in range(W):
        if a[color - 1] == 0:
            color += 1
        if i % 2 == 0:
            ans[i][j] = color
            a[color - 1] -= 1
        else:
            ans[i][-j - 1] = color
            a[color - 1] -= 1

for i in range(H):
    print(*ans[i])