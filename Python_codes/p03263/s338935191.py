def abc109_d():
    h, w = (int(x) for x in input().split())
    grid = [[int(x) for x in input().split()] for _ in range(h)]

    move = []
    rest = []
    for i in range(h):
        pick = False
        for j in range(w):
            v = grid[i][j]
            if pick:
                if v%2:
                    pick = False
                else:
                    if j < w-1: move.append((i+1, j+1, i+1, j+2))
            else:
                if v%2:
                    pick = True
                    if j < w-1: move.append((i+1, j+1, i+1, j+2))
        rest.append(pick)

    pick = False
    for i, v in enumerate(rest):
        if pick:
            if v:
                pick = False
            else:
                if i < h-1: move.append((i+1, w, i+2, w))
        else:
            if v%2:
                pick = True
                if i < h-1: move.append((i+1, w, i+2, w))

    print(len(move))
    for mv in move:
        print(*mv, sep=' ')

if __name__ == '__main__':
    abc109_d()