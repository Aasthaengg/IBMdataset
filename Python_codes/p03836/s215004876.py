sx, sy, tx, ty = map(int, input().split())

ans = ''
if sy < ty:
  v = 'U' * (ty-sy)
  if sx < tx:
    h = 'R' * (tx-sx)
    ans += v + h
    v = 'D' * (ty-sy)
    h = 'L' * (tx-sx)
    ans += v + h
  else:
    h = 'L' * (tx-sx)
    ans += v + h
    v = 'D' * (ty-sy)
    h = 'R' * (tx-sx)
    ans += v + h
else:
  v = 'D' * (sy-ty)
  if sx < tx:
    h = 'R' * (tx-sx)
    ans += v + h
    v = 'U' * (ty-sy)
    h = 'L' * (tx-sx)
    ans += v + h
  else:
    h = 'L' * (tx-sx)
    ans += v + h
    v = 'U' * (ty-sy)
    h = 'R' * (tx-sx)
    ans += v + h
  
if sy < ty:
  v = 'U' * (ty-sy+1)
  if sx < tx:
    h = 'R' * (tx-sx+1)
    ans += 'L' + v + h + 'D'
    v = 'D' * (ty-sy+1)
    h = 'L' * (tx-sx+1)
    ans += 'R' + v + h + 'U'
  else:
    h = 'L' * (tx-sx+1)
    ans += 'R' + v + h + 'D'
    v = 'D' * (ty-sy+1)
    h = 'R' * (tx-sx+1)
    ans += 'L' + v + h + 'U'
else:
  v = 'D' * (sy-ty+1)
  if sx < tx:
    h = 'R' * (tx-sx+1)
    ans += 'L' + v + h + 'U'
    v = 'U' * (ty-sy+1)
    h = 'L' * (tx-sx+1)
    ans += 'R' + v + h + 'D'
  else:
    h = 'L' * (tx-sx+1)
    ans += 'R' + v + h + 'U'
    v = 'U' * (ty-sy+1)
    h = 'R' * (tx-sx+1)
    ans += 'L' + v + h + 'D'
print(ans)