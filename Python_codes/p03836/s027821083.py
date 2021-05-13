
sx,sy,tx,ty = map(int,input().split())
for i in range(tx-sx):
    print("R",end = "")
for i in range(ty-sy):
    print("U",end = "")
for i in range(tx-sx):
    print("L",end = "")
for i in range(ty-sy):
    print("D",end = "")
print("D",end = "")
for i in range(tx-sx+1):
    print("R",end = "")
for i in range(ty-sy+1):
    print("U",end = "")
print("L",end = "")
print("U",end = "")
for i in range(tx-sx+1):
    print("L",end = "")
for i in range(ty-sy+1):
    print("D",end = "")
print("R")