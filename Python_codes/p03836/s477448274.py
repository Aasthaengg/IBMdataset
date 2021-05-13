sx,sy,tx,ty=map(int,input().split())

iki=["U" for i in range(ty-sy)]+["R" for i in range(tx-sx)]
kaeri=["D" for i in range(ty-sy)]+["L" for i in range(tx-sx)]
iki2=["L"]+["U" for i in range(ty-sy+1)]+["R" for i in range(tx-sx+1)]+["D"]
kaeri2=["R"]+["D" for i in range(ty-sy+1)]+["L" for i in range(tx-sx+1)]+["U"]
ans=iki+kaeri+iki2+kaeri2
print(*ans,sep="")