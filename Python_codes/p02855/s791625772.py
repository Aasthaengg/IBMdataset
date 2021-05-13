if __name__ == '__main__':
    h, w, k = map(int, input().split())
    field = [list(input()) for i in range(h)]
    cnt = 1
    for y in range(h):
        for x in range(w):
            if field[y][x] == "#":
                field[y][x] = cnt
                cnt += 1

    for y in range(h):
        for x in range(w):
            if field[y][x] == "." and x - 1 >= 0:
                field[y][x] = field[y][x - 1]

    for y in range(h):
        for x in list(reversed(range(w))):
            if field[y][x] == "." and x + 1 < w:
                field[y][x] = field[y][x + 1]

    for x in range(w):
        for y in range(h):
            if field[y][x] == "." and y - 1 >= 0:
                field[y][x] = field[y - 1][x]

    for x in range(w):
        for y in list(reversed(range(h))):
            if field[y][x] == "." and y + 1 < h:
                field[y][x] = field[y + 1][x]

    for y in range(h):
        for x in range(w):
            print("{} ".format(field[y][x]), end='')
        print()
