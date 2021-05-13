sx,sy,tx,ty = map(int,input().split())
ans = ""
y = ty-sy
x = tx-sx
ans += "U"*y+"R"*x+"D"*y+"L"*(x+1)+"U"*(y+1)+"R"*(x+1)+"DR"+"D"*(y+1)+"L"*(x+1)+"U"
print(ans)