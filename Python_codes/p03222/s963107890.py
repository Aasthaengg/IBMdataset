H, W, K = map(int, input().split())
mod = 10**9 + 7
draw_array = [1, 1, 2, 3, 5, 8, 13, 21, 34]

if W == 1:
    print(1)
    exit()

ans_array = [[0] * W for i in range(H)]

ans_array[0][0] = draw_array[W - 1]
ans_array[0][1] = draw_array[W - 2]

for i in range(1, H):
    for w in range(W):
        if w == 0:
            ans_array[i][w] = (ans_array[i - 1][w] * draw_array[W - 1]) + (
                ans_array[i - 1][w + 1] * draw_array[W - 2])
            ans_array[i][w] = ans_array[i][w] % mod
        elif w == W - 1:
            ans_array[i][w] = (ans_array[i - 1][w] * draw_array[W - 1]) + (
                ans_array[i - 1][w - 1] * draw_array[W - 2])
            ans_array[i][w] = ans_array[i][w] % mod
        else:
            from_left = ans_array[i - 1][w - 1] * (
                draw_array[w - 1] * draw_array[W - w - 1])
            from_left = from_left % mod
            from_center = ans_array[i - 1][w] * (
                draw_array[w] * draw_array[W - w - 1])
            from_center = from_center % mod
            from_right = ans_array[i - 1][w + 1] * (
                draw_array[w] * draw_array[W - w - 2])
            from_right = from_right % mod
            ans_array[i][w] = (from_left+from_center+from_right) % mod

# print(ans_array)
print(ans_array[H-1][K-1])
