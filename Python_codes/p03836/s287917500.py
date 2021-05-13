sx, sy, tx, ty = list(map(int, input().split()))

sol = ""
sol += "R"*(tx-sx) + "U"*(ty-sy) + "L"*(tx-sx) + "D"*(ty-sy)
sol += "D"+ "R"*(tx-sx + 1) + "U"*(ty-sy + 1) + "LU" + "L"*(tx-sx + 1) + "D"*(ty-sy+1) + "R"

print(sol)