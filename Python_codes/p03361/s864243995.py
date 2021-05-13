h,w = map(int,input().split())
grid = [list(input()) for i in range(h)]

def judge (y,x):
    if y == 0:
        if x == 0:
            # gridの一番左上 → 右か下が # ならOK
            if grid[y][x+1] == '#' or grid[y+1][x] == '#':
                return True
            else:
                return False
        elif x == w-1:
            # gridの一番右上 → 左か下が # ならOK
            if grid[y][x-1] == '#' or grid[y+1][x] == '#':
                return True
            else:
                return False
        else:
            # girdの一番上列 → 左右か下が # ならOK
            if grid[y][x-1] == '#' or grid[y+1][x] == '#' or grid[y][x+1] == '#':
                return True
            else:
                return False
    elif y == h-1:
        if x == 0:
            # gridの一番左下 → 右か上が # ならOK
            if grid[y][x+1] == '#' or grid[y-1][x] == '#':
                return True
            else:
                return False
        elif x == w-1:
            # gridの一番右下 → 左か上が # ならOK
            if grid[y][x-1] == '#' or grid[y-1][x] == '#':
                return True
            else:
                return False
        else:
            # girdの一番下列 → 左右か上が # ならOK
            if grid[y][x-1] == '#' or grid[y-1][x] == '#' or grid[y][x+1] == '#':
                return True
            else:
                return False
    elif x == 0:
        # grid の一番左列。左上と左下のパターンは考えなくてOK
        if grid[y][x+1] == '#' or grid[y-1][x] == '#' or grid[y+1][x] == '#':
            return True
        else:
            return False
    elif x == w-1:
        # grid の一番右列。右上と右下のパターンは考えなくてOK
        if grid[y][x-1] == '#' or grid[y-1][x] == '#' or grid[y+1][x] == '#':
            return True
        else:
            return False
    else:
        # 端っこの列じゃない場合
        if grid[y+1][x] == '#' or grid[y-1][x] == '#' or grid[y][x+1] == '#' or grid[y][x-1] == '#':
            return True
        else:
            return False

for line in range(h):
    for p in range(w):
        if grid[line][p] == "#":
            if judge (line,p):
                pass
            else:
                print ("No")
                exit ()
print ("Yes")
