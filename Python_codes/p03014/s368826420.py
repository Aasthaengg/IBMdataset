H, W = map(int, input().split())
S = [[c == "." for c in input()] for _ in range(H)]
to_right = [[0] * W for _ in range(H)]
to_left = [[0] * W for _ in range(H)]
for i in range(H):
    right = 0
    left = 0
    for j in range(W):
        if S[i][j]:
            right += 1
        else:
            right = 0
        to_right[i][j] = right
        if S[i][-(j + 1)]:
            left += 1
        else:
            left = 0
        to_left[i][-(j + 1)] = left
to_bottom = [[0] * W for _ in range(H)]
to_top = [[0] * W for _ in range(H)]
for j in range(W):
    bottom = 0
    top = 0
    for i in range(H):
        if S[i][j]:
            bottom += 1
        else:
            bottom = 0
        to_bottom[i][j] = bottom
        if S[-(i + 1)][j]:
            top += 1
        else:
            top = 0
        to_top[-(i + 1)][j] = top
ans = 0
for i in range(H):
    right = 0
    left = 0
    for j in range(W):
        if not S[i][j]:
            continue
        ans = max(ans, sum((to_right[i][j], to_left[i][j], to_bottom[i][j], to_top[i][j])))
print(ans - 3)