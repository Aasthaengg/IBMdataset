H,W = map(int,input().split())
t = [list(input()) for _ in range(H)]
udlr = [[-1, 0],[ 1, 0],[ 0,-1],[ 0, 1]]
#[print(line) for line in t];print()

exist_F_count = 0
for i in range(H):
    for j in range(W):
        if t[i][j] == "#":
            exist = False
            for x,y in udlr:
                if (0 <= i+x < H) and (0 <= j+y < W):
                    if t[i+x][j+y] == "#":
                        exist = True
                        break
            if exist == False:
                exist_F_count += 1
                print("No")
                exit()
if exist_F_count == 0:
    print("Yes")