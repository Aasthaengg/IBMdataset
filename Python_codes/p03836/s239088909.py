#!/usr/bin/env python3
s_x, s_y, t_x, t_y = map(int, input().split())
ans = ""
ans += "R" * (t_x - s_x) + "U" * (t_y - s_y)
ans += "L" * (t_x - s_x) + "D" * (t_y - s_y)
ans += "D" + "R" * (t_x - s_x + 1) + "U" * (t_y - s_y + 1) + "L"
ans += "U" + "L" * (t_x - s_x + 1) + "D" * (t_y - s_y + 1) + "R"
print(ans)
