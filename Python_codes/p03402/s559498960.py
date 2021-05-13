a, b = map(int, input().split())
y, x = 1, 1 
moves = ((1, 0), (0, 1), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1))

if a <= b:
    c1, c2 = '.', '#'
    res = [['.']*100 for _ in range(100)]
else:
    c1, c2 = '#', '.'
    a, b = b, a
    res = [['#']*100 for _ in range(100)]

while a > 1 and b > 1:
    res[y][x] = c1
    for dy, dx in moves:
        res[y+dy][x+dx] = c2

    x += 4
    if x > 98:
        y += 4
        x = 1

    a -= 1
    b -= 1

    
for i in range(b):
    res[y][x] = c2
    x += 2
    if x > 98:
        y += 4
        x = 1

print(100, 100)
for h in range(100):
    print(''.join(res[h]))
