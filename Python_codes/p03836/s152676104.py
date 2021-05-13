sx, sy, tx, ty = map(int, input().split())
py = ty-sy
px = tx-sx
ans = "R"*px + "U"*py + "L"*px + "D"*(py+1) + "R"*(px+1) + "U"*(py+1) + "LU" + "L"*(px+1) + "D"*(py+1)+ "R" 
 
print(ans)