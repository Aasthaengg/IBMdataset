h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for y in range(h):
    for x in range(w):
        if s[y][x] == ".":
            continue
        if 0 < x < w-1:
            if 0 < y < h-1:
                if s[y][x-1] == "." and s[y][x+1] == "." and s[y-1][x] == "." and s[y+1][x] == ".":
                    print("No")
                    exit()
            elif y == 0:
                if s[y][x-1] == "." and s[y][x+1] == "." and s[y+1][x] == ".":
                    print("No")
                    exit()
            else:
                if s[y][x-1] == "." and s[y][x+1] == "." and s[y-1][x] == ".":
                    print("No")
                    exit()
        elif x == 0:
            if 0 < y < h-1:
                if s[y][x+1] == "." and s[y-1][x] == "." and s[y+1][x] == ".":
                    print("No")
                    exit()
            elif y == 0:
                if s[y][x+1] == "." and s[y+1][x] == ".":
                    print("No")
                    exit()
            else:
                if s[y][x+1] == "." and s[y-1][x] == ".":
                    print("No")
                    exit()
        else:
            if 0 < y < h-1:
                if s[y][x-1] == "." and s[y-1][x] == "." and s[y+1][x] == ".":
                    print("No")
                    exit()
            elif y == 0:
                if s[y][x-1] == "." and s[y+1][x] == ".":
                    print("No")
                    exit()
            else:
                if s[y][x-1] == "." and s[y-1][x] == ".":
                    print("No")
                    exit()
print("Yes")