sx, sy, gx, gy = map(int, input().split())
gx -= sx
gy -= sy
print('R' * gx, end='')
print('U' * gy, end='')
print('L' * gx, end='')
print('D' * gy, end='')
print('D', end='')
print('R' * (gx+1), end='')
print('U' * (gy+1), end='')
print('L', end='')
print('U', end='')
print('L' * (gx+1), end='')
print('D' * (gy+1), end='')
print('R')