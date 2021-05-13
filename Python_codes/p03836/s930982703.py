sx,sy,tx,ty = map(int,input().split())

dx = tx-sx
dy = ty-sy

print(dy*"U"+dx*"R"+dy*"D"+dx*"L"+"L"+(dy+1)*"U"+(dx+1)*"R"+"D"+"R"+(dy+1)*"D"+(dx+1)*"L"+"U")
