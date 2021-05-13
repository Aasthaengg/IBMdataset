# AtCoder
H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))

ans = [[0]*W for i in range(H)]
cu = 0
for y in range(H):
    for x in range(W):
        ans[y][x] = cu + 1
        a[cu] -= 1
        if not a[cu]:
            cu += 1

for i in range(H):
    if i % 2 != 0:
        print(' '.join(map(str, sorted(ans[i], reverse=True))))
    else:
        print(' '.join(map(str, ans[i])))
