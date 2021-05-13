sx, sy, tx, ty = map(int, input().split())

p1 = 'U' * (ty - sy) + 'R' * (tx - sx)
p2 = 'U' + 'L' * (tx - sx + 1) + 'D' * (ty - sy + 1) + 'R'
p3 = p1[::-1]
p4 = p2[::-1]

print(p1 + p2 + p3 + p4)