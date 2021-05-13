h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

ans = []
for i in range(h):
    for j in range(w):
        if int(a[i][j]) % 2 == 1:
            # i < h-1なら下に移動
            if i < h-1:
                ans.append([i, j, i+1, j])
                a[i+1][j] += 1
                a[i][j] -= 1
            else:
                # j < w-1なら右に移動
                if j < w-1:
                    ans.append([i, j, i, j+1])
                    a[i][j+1] += 1
print(len(ans))
for an in ans:
    print(*[i+1 for i in an])
