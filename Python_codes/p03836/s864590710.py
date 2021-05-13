sx,sy,tx,ty = map(int,input().split())
ans = ''
if tx - sx > 0:
  if ty - sy > 0:
    x = ['R','L','U','D']
  else:
    x = ['R','L','D','U']
else:
  if ty - sy > 0:
    x = ['L','R','U','D']
  else:
    x = ['L','R','D','U']
ans += x[0]*abs(tx-sx)
ans += x[2]*abs(sy-ty)
ans += x[1]*abs(tx-sx)
ans += x[3]*abs(ty-sy)
ans += x[3] + x[0]*(abs(tx-sx)+1)
ans += x[2]*(abs(ty-sy)+1) + x[1]
ans += x[2] + x[1]*(abs(tx-sx)+1)
ans += x[3]*(abs(ty-sy)+1) + x[0]
print(ans)