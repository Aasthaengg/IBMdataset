sx,sy,tx,ty=map(int,input().split())
tempx=tx-sx
tempy=ty-sy
ans=["R"]*tempx+["U"]*tempy+["L"]*tempx+["D"]*tempy+["D"]+["R"]*(tempx+1)+["U"]*(tempy+1)+["L"]+["U"]+["L"]*(tempx+1)+["D"]*(tempy+1)+["R"]
print("".join(ans))