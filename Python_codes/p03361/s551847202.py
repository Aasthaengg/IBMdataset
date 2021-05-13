H, W = map(int, input().split(" "))

area = [["." for _ in range(W+2)]]
for _ in range(H):
    line = [d for d in ("."+input()+".")]
    area.append(line)
area.append(["." for _ in range(W+2)])
    
def distinct(x,y):
    if area[y+1][x] == "#" or area[y-1][x] == "#" or \
        area[y][x+1] == "#" or area[y][x-1] == "#":
        return 0
    else:
        return 1
    
flg = 0
for y in range(1,H+1):
    for x in range(1,W+1):
        if area[y][x] == "#":
            if distinct(x,y) == 1:
                flg = 1
                break
    if flg == 1:
        break

if flg == 0:
    print("Yes")
else:
    print("No")
