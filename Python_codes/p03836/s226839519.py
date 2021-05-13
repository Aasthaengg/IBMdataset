def addRoute(i, c):
  t = ''
  for _ in range(i):
    t += c
  return t

pos=list(map(int, input().split()))
ud = pos[3] - pos[1]
rl = pos[2] - pos[0]
s = ''

s += addRoute(ud, 'U')
s += addRoute(rl, 'R')
s += addRoute(ud, 'D')
s += addRoute(rl, 'L')
s += 'L'
s += addRoute(ud+1, 'U')
s += addRoute(rl+1, 'R')
s += 'DR'
s += addRoute(ud+1, 'D')
s += addRoute(rl+1, 'L')
s += 'U'
print(s)