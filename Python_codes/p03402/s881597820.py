A,B = map(int,input().split())
cnt = 0
grid = []

for i in range(50):
    s = ''
    for j in range(25):
        k = 0
        if i%2 == 0 and cnt < A-1:
            s += '.###'
            cnt += 1
            k = 1
        if i%2 == 1 and cnt < A-1:
            s += '##.#'
            cnt += 1
            k = 1
        if k == 0:
            s += '####'
    grid.append(s)
s = ''
for i in range(100):
    s += '.'
grid.append(s)
cnt = 0
for i in range(49):
    s = ''
    for j in range(25):
        k = 0
        if i%2 == 0 and cnt < B-1:
            s += '#...'
            cnt += 1
            k = 1
        if i%2 == 1 and cnt < B-1:
            s += '..#.'
            cnt += 1
            k = 1
        if k == 0:
            s += '....'
    grid.insert(50,s)

print(100,100)
for i in range(100):
    print(grid[i])