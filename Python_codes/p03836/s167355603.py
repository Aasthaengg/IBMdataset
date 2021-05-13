sx,sy,gx,gy = (int(x) for x in input().split())
ans = ''
if sx < gx and sy < gy:
  ans += 'R'*(gx-sx) + 'U'*((gy-sy)+1) + 'L'*((gx-sx)+1) + 'D'*((gy-sy)+1) + 'R'
  ans += 'D' + 'R'*((gx-sx)+1) + 'U'*((gy-sy)+1) + 'L'*((gx-sx)+1) + 'D'*(gy-sy)
elif sx < gx and sy > gy:
  ans += 'R'*(gx-sx) + 'U'*((gy-sy)+1) + 'L'*((gx-sx)+1) + 'D'*((gy-sy)+1) + 'R'
print (ans)
