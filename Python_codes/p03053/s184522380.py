H, W = map(int, input().split())
fields = [list(map(lambda c: c == '#', input())) for _ in range(H)]

checking = []
for i, row in enumerate(fields):
    for j, elem in enumerate(row):
        if elem:
            checking.append( (i, j) )

counter = 0
while True:
    to_check = []
    for y, x in checking:
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if 0 <= x+dx < W and 0 <= y+dy < H and not fields[y+dy][x+dx]:
                fields[y+dy][x+dx] = True
                to_check.append( (y+dy, x+dx) )

    if not to_check:
        break
    checking = to_check
    counter += 1

print(counter)
