sx, sy, tx, ty = map(int, input().split())

dy = tx - sx
dx = ty - sy

ans = ''

ans += 'U' * dx
ans += 'R' * dy
ans += 'D' * dx
ans += 'L' * dy
ans += 'L'
ans += 'U' * (dx + 1)
ans += 'R' * (dy + 1)
ans += 'D'
ans += 'R'
ans += 'D' * (dx + 1)
ans += 'L' * (dy + 1)
ans += 'U'

print(ans)