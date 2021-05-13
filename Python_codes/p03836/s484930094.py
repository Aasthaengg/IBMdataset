
sx,sy,tx,ty=map(int,input().split())
x=tx-sx
y=ty-sy

p1="U"*y+"R"*x
p2="D"*y+"L"*x
p3="L"+"U"*(y+1)+"R"*(x+1)+"D"
p4="R"+"D"*(y+1)+"L"*(x+1)+"U"

print(p1+p2+p3+p4)