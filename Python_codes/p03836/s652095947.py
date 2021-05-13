sx, sy, tx, ty = map(int, input().split())
x = tx - sx
y = ty - sy
L = []
L.append('R' * x)
L.append('U' * y)
L.append('L' * x)
L.append('D' * (y + 1))
L.append('R' * (x + 1))
L.append('U' * (y + 1))
L.append('LU')
L.append('L' * (x + 1))
L.append('D' * (y + 1))
L.append('R')
print(*L, sep='')
