H, W = map(int, input().split(" "))

maps = [[0 for _ in range(W+2)]]

for _ in range(H):
    line = [dot for dot in ("."+input()+".")]
    line_ = [1 if point == "#" else 0 for point in line]
    maps.append(line_)
maps.append([0 for _ in range(W+2)])

    
def calc(x, y):
    return maps[y-1][x] + maps[y+1][x] + maps[y][x+1] + maps[y][x-1] \
            + maps[y+1][x+1] + maps[y-1][x-1] + maps[y+1][x-1] + maps[y-1][x+1]

for y in range(1,H+1):
    for x in range(1,W+1):
        if maps[y][x] != 1:
            print(calc(x,y), end="")
        else:
            print("#",end= "")
    print()
