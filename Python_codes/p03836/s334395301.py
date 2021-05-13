sx, sy, tx, ty = map(int, input().split())
# x→yの順に処理していけば良い。
iki_x = tx - sx
iki_y = ty - sy
ans = ""
ans += "R" * iki_x
ans += "U" * iki_y
ans += "L" * iki_x
ans += "D" * iki_y
ans += "D"
ans += "R" * (iki_x + 1)
ans += "U" * (iki_y + 1)
ans += "L"
ans += "U"
ans += "L" * (iki_x + 1)
ans += "D" * (iki_y + 1)
ans += "R"
print(ans)
