H, W = map(int, input().split())
sl = [input() for _ in range(H)]

ans = "Yes"
for i, s in enumerate(sl):
    for j, p in enumerate(s):
        if sl[i][j] == ".":
            continue
        up_s = sl[i - 1][j] if i - 1 >= 0 else ""
        down_s = sl[i + 1][j] if i + 1 < H else ""
        left_s = sl[i][j - 1] if j - 1 >= 0 else ""
        right_s = sl[i][j + 1] if j + 1 < W else ""
        if "#" in [up_s, down_s, left_s, right_s]:
            continue
        ans = "No"
        break
    if ans == "No":
        break

print(ans)
