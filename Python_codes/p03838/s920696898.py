st, gl = map(int, input().split())
ans = 0

if gl == -st:
  ans = 1
elif st >= 0:
  if gl > st:
    ans = gl - st
  elif gl < -st:
    ans = - st - gl + 1
  elif gl > 0:
    ans = st - gl + 2
  else:
    ans = gl + st + 1
elif st < 0:
  if gl > -st:
    ans = gl + st + 1
  elif gl < st:
    ans = st - gl + 2
  elif gl > 0:
    ans = - st - gl + 1
  else:
    ans = gl - st
  
print(ans)
