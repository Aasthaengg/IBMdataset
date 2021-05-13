H, W = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(H)]

flag = False
h, w = 1, 1
ans = []


def it_grid(h, w):
    if h % 2:
        if w == W:
            h += 1
        else:
            w += 1
    else:
        if w == 1:
            h += 1
        else:
            w -= 1
    return h, w


while h <= H:
    new_h, new_w = it_grid(h, w)
    if A[h - 1][w - 1] % 2:
        if not flag and new_h <= H:
            ans.append((h, w, new_h, new_w))
        flag = not flag
    else:
        if flag and new_h <= H:
            ans.append((h, w, new_h, new_w))
    h, w = new_h, new_w

print(len(ans))
for t in ans:
    print(*t)
