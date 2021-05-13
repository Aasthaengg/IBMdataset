sx,sy,tx,ty = map(int,input().split())

dx = tx-sx
dy = ty-sy
res =''
#1回目
for _ in range(dx): res += 'R'
for _ in range(dy): res += 'U'
for _ in range(dx): res += 'L'
for _ in range(dy): res += 'D'
#2回目
res += 'D'
for _ in range(dx+1): res += 'R'
for _ in range(dy+1): res += 'U'
res += "L"
res += "U"
for _ in range(dx+1): res += 'L'
for _ in range(dy+1): res += 'D'
res += 'R'
print(res)