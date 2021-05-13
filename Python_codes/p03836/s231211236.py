sx, sy, tx, ty = map(int, input().split())

dx = tx - sx
dy = ty - sy

route1 = 'R' * dx + 'U' * dy
route2 = 'L' * dx + 'D' * dy
route3 = 'L' + 'U' * (dy + 1) + 'R' * (dx + 1) + 'D'
route4 = 'R' + 'D' * (dy + 1) + 'L' * (dx + 1) + 'U'

ans = route1 + route2 + route3 + route4
print(ans)
