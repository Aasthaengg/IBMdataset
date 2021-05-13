sx, sy, tx, ty = map(int, input().split())

s = ''
for _ in range(ty - sy):
    s += 'U'

for _ in range(tx - sx):
    s += 'R'

for _ in range(ty - sy):
    s += 'D'

for _ in range(tx - sx):
    s += 'L'

s += 'L'

for _ in range(ty - sy + 1):
    s += 'U'

for _ in range(tx - sx + 1):
    s += 'R'

s += 'DR'

for _ in range(ty - sy + 1):
    s += 'D'

for _ in range(tx - sx + 1):
    s += 'L'

s += 'U'

print(s)
