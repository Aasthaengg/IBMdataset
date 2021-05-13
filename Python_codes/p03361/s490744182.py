h, w = map(int,input().split())
li = [list(input()) for i in range(h)]

if h == 1 or w == 1:
    print("No")
    exit()

for i in range(h):
    for j in range(w):
        x = 0 #縦OK
        y = 0 #横OK
        if li[i][j] == "#":
            if i == 0:
                if li[i+1][j] == "#":
                    x = 1
            elif i == h-1:
                if li[i-1][j] == "#":
                    x = 1
            else:
                if li[i+1][j] == "#" or li[i-1][j] == "#":
                    x = 1
            if j == 0:
                if li[i][j+1] == "#":
                    y = 1
            elif j == w-1:
                if li[i][j-1] == "#":
                    y = 1
            else:
                if li[i][j+1] == "#" or li[i][j-1] == "#":
                    y = 1 

            if x == 0 and y == 0:
                print("No")
                exit()

print("Yes")