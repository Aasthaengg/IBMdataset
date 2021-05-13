sx, sy, tx, ty = map(int, input().split())
dx = tx - sx
dy = ty - sy

moves = ''

# s -> t (1)
moves += 'U' * dy
moves += 'R' * dx
# t -> s (1)
moves += 'D' * dy
moves += 'L' * dx

# s -> t (2)
moves += 'L'
moves += 'U' * (dy + 1)
moves += 'R' * (dx + 1)
moves += 'D'

# t -> s (2)
moves += 'R'
moves += 'D' * (dy + 1)
moves += 'L' * (dx + 1)
moves += 'U'

print(moves)