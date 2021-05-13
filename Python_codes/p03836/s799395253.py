sx, sy, tx, ty = list(map(int, input().split()))

out = []
dx = tx - sx
dy = ty - sy
out.append('R' * dx)
out.append('U' * dy)
out.append('L' * dx)
out.append('D' * dy)
out.append('D')
out.append('R' * (dx + 1))
out.append('U' * (dy + 1))
out.append('L')
out.append('U')
out.append('L' * (dx + 1))
out.append('D' * (dy + 1))
out.append('R' * 1)
print(''.join(out))
