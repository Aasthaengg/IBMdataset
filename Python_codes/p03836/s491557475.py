sx,sy,tx,ty=map(int,input().split())
ans=""
d=(tx-sx)+(ty-sy)#sとtの距離
#1週目　最短距離
for i in range(2*d):
    if i<=(tx-sx)-1:
        ans+="R"
    elif i<=d-1:
        ans+="U"
    elif i<=(d-1)+(tx-sx):
        ans+="L"
    else:
        ans+="D"
#print(ans)
#2週目 外周
for j in range(2*(d+4)):
    if j==0:
        ans+="D"
    elif j<=(tx-sx)+2-1:
        ans+="R"
    elif j<=(d+4)-1-1:
        ans+="U"
    elif j<=(d+4)-1:
        ans+="L"
    elif j<=(d+4)-1+1:
        ans+="U"
    elif j<=(d+4)-1+1+(tx-sx+1):
        ans+="L"
    elif j<=2*(d+4)-1-1:
        ans+="D"
    else:
        ans+="R"
print(ans)