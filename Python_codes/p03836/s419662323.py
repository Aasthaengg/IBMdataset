sx, sy, tx, ty = map(int, input().split())

dx = tx - sx
dy = ty - sy
path1 = 'U' * dy + 'R' * dx
path2 = 'D' * dy + 'L' * dx
path3 = 'L' + 'U' * (dy+1) + 'R' * (dx+1) + 'D'
path4 = 'R' + 'D' * (dy+1) + 'L' * (dx+1) + 'U'
print(path1 + path2 + path3 + path4)