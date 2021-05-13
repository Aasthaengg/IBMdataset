sx,sy,tx,ty=map(int,input().split())
dx=tx-sx
dy=ty-sy
ans=""
for i in range(dy):
    ans+="U"
for j in range(dx):
    ans+="R"
for i in range(dy):
    ans+="D"
for j in range(dx):
    ans+="L"
ans+="L"
for i in range(dy+1):
    ans+="U"
for i in range(dx+1):
    ans+="R"
ans+="DR"
for i in range(dy+1):
    ans+="D"
for i in range(dx+1):
    ans+="L"
ans+="U"
print(ans)