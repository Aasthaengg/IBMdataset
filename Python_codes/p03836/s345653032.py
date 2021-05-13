sx, sy, tx, ty = list(map(int, input().split()))
dy = abs(ty-sy)
dx = abs(tx-sx)
# 1巡目
ans = ''
ans += 'U'*(dy)
ans += 'R'*(dx)
ans += 'D'*(dy)
ans += 'L'*(dx)
# 2巡目
ans += 'L'
ans += 'U'*(dy+1)
ans += 'R'*(dx+1)
ans += 'D'
ans += 'R'
ans += 'D'*(dy+1)
ans += 'L'*(dx+1)
ans += 'U'

print(ans)
