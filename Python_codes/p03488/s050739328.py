s = input().split('T')
s = [len(_s) for _s in s]
x, y = map(int, input().split())
dx = s[::2]
dy = [0]+s[1::2]

def check(dz, z, base=8001, first_fixed=True):
  a = dz[0]
  if first_fixed:
    state = 1 << base + a
  else:
    state = 1 << (base + a) | 1 << (base - a) 
  for a in dz[1:]:
    state = (state<<a | state>>a)
  return (state>>(base+z)) & 1

if check(dx, x) and check(dy, y, first_fixed=False):
  print('Yes')
else:
  print('No')