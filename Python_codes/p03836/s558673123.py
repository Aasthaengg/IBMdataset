sx,sy,tx,ty = map(int, input().split())

dx = tx - sx
dy = ty - sy

xdir = "R" if dx >= 0 else "L"
xdir_r = "L" if dx >= 0 else "R"
ydir = "U" if dy >= 0 else "D"
ydir_r = "D" if dy >= 0 else "U"

ans = ans_r = ""
ans_2 = ans_2_r = ""
ans += xdir * abs(dx) + ydir * abs(dy)
ans_r += xdir_r * abs(dx) + ydir_r * abs(dy)

ans_2 += ydir_r + xdir * (abs(dx) + 1) + ydir * (abs(dy) + 1) + xdir_r
ans_2_r += ydir + xdir_r * (abs(dx) + 1) + ydir_r * (abs(dy) + 1) + xdir
print(ans + ans_r + ans_2 + ans_2_r)