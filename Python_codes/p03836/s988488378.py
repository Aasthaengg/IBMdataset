sx, sy, tx, ty = map(int, input().split())
ans = ""

diff_x = abs(tx-sx)
diff_y = abs(ty-sy)

# 最短距離で行って戻る
ans += "U" * diff_y + "R" * diff_x
ans += "D" * diff_y + "L" * diff_x

# 一歩左に進んでから、ty+1の位置まで上に進む。
ans += "L" * 1 + "U" * (diff_y+1)
# txの位置まで右に進んでから、一歩下に進む。
ans += "R" * (diff_x+1) + "D" * 1

# 一歩右に進んでから、sy-1の位置まで下に進む。
ans += "R" * 1 + "D" * (diff_y+1)
# sxの位置まで左に進んでから、一歩上に進む。
ans += "L" * (diff_x+1) + "U" * 1

print(ans)
