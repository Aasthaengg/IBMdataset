sx,sy,tx,ty = map(int,input().split())

Ans1 = []
Ans2 = []
dx = tx - sx
dy = ty - sy
cnt = abs(dx) + abs(dy)
if dy > 0:
    for i in range(dy):
        Ans1.append("U")
        Ans2.append("D")
else:
    for i in range(-dy):
        Ans1.append("D")
        Ans2.append("U")
if dx > 0:
    for i in range(dx):
        Ans1.append("R")
        Ans2.append("L")
else:
    for i in range(-dx):
        Ans1.append("L")
        ANs2.append("R")

add1 = ["L","U"]
add2 = ["R","D"]

print("".join(Ans1) ,end="")
print("".join(Ans2) ,end="")

if Ans1[0] == "U":
    print("".join(add1),end="")
    print("".join(Ans1) ,end="")
    print("".join(add2),end = "")
    print("".join(add2),end="")
    print("".join(Ans2) ,end="")
    print("".join(add1))
else:
    print("".join(add2),end="")
    print("".join(Ans1) ,end="")
    print("".join(add1),end="")
    print("".join(add1),end="")
    print("".join(Ans2) ,end="")
    print("".join(add2))