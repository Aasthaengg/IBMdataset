a, b = map(int, input().split())

x, y = '.', '#'
if a > b:
    a, b = b, a
    x, y = y, x

space = [[x for _ in range(100)] for _ in range(100)]

for z in range(b):
    i, j = divmod(z, 25)
    for di in range(3):
        for dj in range(3):
            space[i*4+di][j*4+dj] = y

for z in range(a-1):
    i, j = divmod(z, 25)
    space[i*4+1][j*4+1] = x

print("100 100")
print('\n'.join((''.join(row)) for row in space))