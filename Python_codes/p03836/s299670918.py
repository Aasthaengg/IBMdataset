sx, sy, gx, gy = map(int, input().split(' '))

route = []
dy = gy - sy
dx = gx - sx
route.append('U' * dy)
route.append('R' * dx)
route.append('D' * dy)
route.append('L' * (dx + 1))
route.append('U' * (dy + 1))
route.append('R' * (dx + 1))
route.append('DR')
route.append('D' * (dy + 1))
route.append('L' * (dx + 1))
route.append('U')
print(''.join(route))
