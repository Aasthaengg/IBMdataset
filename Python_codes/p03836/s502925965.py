sx, sy, tx, ty = map(int, input().split())

go = 'U' * (ty - sy) + 'R' * (tx - sx)
back = 'D' * (ty - sy) + 'L' * (tx - sx)
ans = go + back + 'LU' + go + 'RDRD' + back + 'LU'

print(ans)