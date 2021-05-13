sx,sy,tx,ty = map(int,input().split())
[print("U",end="") for i in range(ty-sy)]
[print("R",end="") for i in range(tx-sx)]
[print("D",end="") for i in range(ty-sy)]
[print("L",end="") for i in range(tx-sx+1)]
[print("U",end="") for i in range(ty-sy+1)]
[print("R",end="") for i in range(tx-sx+1)]
print("D",end="")
print("R",end="")
[print("D",end="") for i in range(ty-sy+1)]
[print("L",end="") for i in range(tx-sx+1)]
print("U")