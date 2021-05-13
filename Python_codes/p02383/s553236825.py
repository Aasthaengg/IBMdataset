up, south, east, west, north, down = map(int, input().split())
command = input()
for c in command:
    if c == 'N':
        copy = north
        north = up
        up = south
        south = down
        down = copy
    elif c == 'S':
        copy = north
        north = down
        down = south
        south = up
        up = copy
    elif c == 'W':
        copy = west
        west = up
        up = east
        east = down
        down = copy
    else:
        copy = west
        west = down
        down = east
        east = up
        up = copy
print(up)

