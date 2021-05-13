r,c = map(int,input().split())

map = []
for i in range(r):
    map.append(input())

def kinbou(y,x):
    sum = 0
    if y-1 >= 0:
        if (map[y-1][x] == '#'):
            sum += 1

    if x-1 >= 0:
        if (map[y][x-1] == '#'):
            sum += 1

    if x+1 < c:
        if (map[y][x+1] == '#'):
            sum += 1

    if y+1 < r:
        if (map[y+1][x] == '#'):
            sum += 1

    if y-1 >= 0 and x-1 >= 0:
        if (map[y-1][x-1] == '#'):
            sum += 1

    if y-1 >= 0 and x+1 < c:
        if (map[y-1][x+1] == '#'):
            sum += 1

    if y+1 < r and x-1 >= 0:
        if (map[y+1][x-1] == '#'):
            sum += 1

    if y+1 < r and x+1 < c:
        if (map[y+1][x+1] == '#'):
            sum += 1
    return sum

map2 = [['0']*c for i in range(r)]

for i in range(r):
    for j in range(c):
        if map[i][j] == '.':
            map2[i][j] = str(kinbou(i,j))
        else:
            map2[i][j] = '#'
    print(''.join(map2[i]))

