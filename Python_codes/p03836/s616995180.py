sx,sy,tx,ty = map(int,input().split())
x = "D"
x += "R"*(tx-sx+1)
x += "U"*(ty-sy+1)
x += "L"
x += "D"*(ty-sy)
x += "L"*(tx-sx)
x += "U"*(ty-sy)
x += "R"*(tx-sx)
x += "U"
x += "L"*(tx-sx+1)
x += "D"*(ty-sy+1)
x += "R"
print(x)