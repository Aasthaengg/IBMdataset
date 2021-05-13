sx,sy,tx,ty = map(int,input().split())
R=[]

R+=["R"]*(tx-sx)
R+=["U"]*(ty-sy)
R+=["L"]*(tx-sx)
R+=["D"]*(ty-sy+1)
R+=["R"]*(tx-sx+1)
R+=["U"]*(ty-sy+1)
R+=["L"]
R+=["U"]
R+=["L"]*(tx-sx+1)
R+=["D"]*(ty-sy+1)
R+=["R"]


print("".join(R))



