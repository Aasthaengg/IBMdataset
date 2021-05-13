H, W = map(int, input().split())
s = [list(str(input())) for i in range(H)]

if s[0][0] == "#":
    if s[0][1] == "." and s[1][0] == ".":
        print("No")
        exit()

if s[0][W-1] == "#":
    if s[0][W-2] == "." and s[1][W-1] == ".":
        print("No")
        exit()

if s[H-1][0] == "#":
    if s[H-1][1] == "." and s[H-2][0] == ".":
        print("No")
        exit()

if s[H-1][W-1] == "#":
    if s[H-1][W-2] == "." and s[H-2][W-1] == ".":
        print("No")
        exit()


for i in range(1, W-1):
    if s[0][i] == "#":
        if s[0][i-1] == "." and s[0][i+1] == "." and s[1][i] ==".":
            print("No")
            exit()
        if s[H-1][i-1] == "." and s[H-1][i+1] == "." and s[H-2][i] ==".":
            print("No")
            exit()

for i in range(1, H-1):
    if s[i][0] == "#":
        if s[i-1][0] == "." and s[i+1][0] == "." and s[i][1] ==".":
            print("No")
            exit()
        if s[i-1][W-1] == "." and s[i+1][W-1] == "." and s[i][W-2] ==".":
            print("No")
            exit()

for i in range(1, H-1):
    for j in range(1, W-1):
        if s[i][j] == "#":
            if s[i-1][j] == "." and s[i+1][j] == "." and s[i][j-1] =="." and s[i][j+1] ==".":
                print("No")
                exit()

print("Yes")
