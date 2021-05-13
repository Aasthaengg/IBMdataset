sx, sy, tx, ty = map(int, input().split())
dx = tx - sx
dy = ty - sy

if dx == 0:
    if dy > 0:
        d1 = "U"
        d2 = "D"
    else:
        d1 = "D"
        d2 = "U"
    dy = abs(dy)
    ans = d1 * dy
    ans += "R" + d2 * dy + "L"
    ans += "L" + d1 * dy + "R"
    ans += d1 + "RR" + d2 * (dy + 2) + "LL" + d1
    print(ans)
    
elif dy == 0:
    if dx > 0:
        d1 = "R"
        d2 = "L"
    else:
        d1 = "L"
        d2 = "R"
    dx = abs(dx)
    ans = d1 * dx
    ans += "U" + d2 * dx + "D"
    ans += "D" + d1 * dx + "U"
    ans += d1 + "UU" + d2 * (dx + 2) + "DD" + d1
    print(ans)

else:
    if dy > 0:
        d1 = "U"
        d2 = "D"
    else:
        d1 = "D"
        d2 = "U"
    if dx > 0:
        d3 = "R"
        d4 = "L"
    else:
        d3 = "L"
        d4 = "R"
    dx = abs(dx)
    dy = abs(dy)
    ans = d1 * dy + d3 * dx
    ans += d2 * dy + d4 * dx
    ans += d4 + d1 * (dy + 1) + d3 * (dx + 1) + d2
    ans += d3 + d2 * (dy + 1) + d4 * (dx + 1) + d1
    print(ans)