sx, sy, tx, ty = map(int, input().split())

res = ''

for _ in range(ty-sy):
    res += 'U'
for _ in range(tx-sx):
    res += 'R'

for _ in range(ty-sy):
    res += 'D'
for _ in range(tx-sx):
    res += 'L'

res += 'LU'
for _ in range(ty-sy):
    res += 'U'
for _ in range(tx-sx):
    res += 'R'
res += 'RD'

res += 'RD'
for _ in range(ty-sy):
    res += 'D'
for _ in range(tx-sx):
    res += 'L'
res += 'LU'

print(res)