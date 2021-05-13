sx,sy,tx,ty=map(int,input().split())
dx=tx-sx
dy=ty-sy

moji=""
moji+="U"*dy+"R"*dx
moji+="U"+"L"*(dx+1)+"D"*(dy+1)+"R"
moji+="D"+"R"*(dx+1)+"U"*(dy+1)+"L"
moji+="D"*(dy)+"L"*(dx)

print(moji)