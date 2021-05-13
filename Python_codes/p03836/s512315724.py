sx,sy,tx,ty=map(int,input().split())

ans=""
for _ in range(tx-sx):
    ans+="R"
for _ in range(ty-sy):
    ans+="U"
for _ in range(tx-sx):
    ans+="L"
for _ in range(ty-sy):
    ans+="D"

ans+="D"
for _ in range(tx-sx+1):
    ans+="R"
for _ in range(ty-sy+1):
    ans+="U"
ans+="L"

ans+="U"
for _ in range(tx-sx+1):
    ans+="L"
for _ in range(ty-sy+1):
    ans+="D"
ans+="R"
print(ans)