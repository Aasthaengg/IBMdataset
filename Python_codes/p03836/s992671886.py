sx, sy, tx, ty = map(int,input().split())

ans = "U"*(ty-sy)
ans += "R"*(tx-sx)
ans += "D"*(ty-sy)
ans += "L"*(tx-sx)

ans += "L"
ans += "U"*(ty+1-sy)
ans += "R"*(tx+1-sx)
ans += "DR"
ans += "D"*(ty-sy+1)
ans += "L"*(tx-sx+1)
ans += "U"

print(ans)