sx, sy, tx, ty = map(int, input().split())

dx, dy = tx - sx, ty - sy

first = 'U' * dy + 'R' * dx
second = 'D' * dy + 'L' * dx
third = 'L' + 'U' * (dy + 1) + 'R' * (dx + 1) + 'D'
forth = 'R' + 'D' * (dy + 1) + 'L' * (dx + 1) + 'U'

print(first + second + third + forth)