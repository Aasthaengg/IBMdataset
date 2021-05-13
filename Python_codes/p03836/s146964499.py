sx,sy,tx,ty = map(int, input().split())
y1=ty-sy
x1=tx-sx
a = "U"*y1+"R"*x1+"D"*y1+"L"*x1+"L"+"U"*(y1+1)+"R"*(x1+1)+"D"+"R"+"D"*(y1+1)+"L"*(x1+1)+"U"
print(a)