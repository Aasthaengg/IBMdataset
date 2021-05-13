sx,sy,tx,ty=map(int,input().split())
x1,y1=tx-sx,ty-sy
x2,y2=x1+2,y1+2

s="U"*y1
s+="R"*x1
s+="D"*y1
s+="L"*x1

s+="L"
s+="U"*(y2-1)
s+="R"*(x2-1)
s+="D"

s+="R"
s+="D"*(y2-1)
s+="L"*(x2-1)
s+="U"

print(s)