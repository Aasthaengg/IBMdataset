sx,sy,tx,ty = map(int,input().split())
a=tx-sx
b=ty-sy
print("U"*b+"R"*a+"D"*b+"L"*a+"L"+"U"*(b+1)+"R"*(a+1)+"D"+"R"+"D"*(b+1)+"L"*(a+1)+"U")
