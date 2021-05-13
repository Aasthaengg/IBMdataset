x_s, y_s, x_t, y_t = map(int, input().split())
dist_x, dist_y = x_t - x_s, y_t - y_s

ans = ""
ans += ("R" * dist_x)
ans += ("U" * dist_y)
ans += ("L" * dist_x)
ans += ("D" * dist_y)
ans += "D"
ans += ("R" * (dist_x + 1))
ans += ("U" * (dist_y + 1))
ans += "LU"
ans += ("L" * (dist_x + 1))
ans += ("D" * (dist_y + 1))
ans += "R"

print(ans)