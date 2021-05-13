def gcd(x, y):
  b = max(x, y)
  s = min(x, y)
  r = b % s
  while r != 0:
    b = s
    s = r
    r = b % s
  return s

def lcm(x, y):
  return (x * y) // gcd(x,y)

def nasu(a, b):
  g = gcd(a, b)
  if g < 0:
    g *= -1
  if b < 0:
    a *= -1
    b *= -1
  return [a // g, b // g]

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

MOD = 10 ** 9 + 7
R = {}

ze = 0
na = 0
su = 0
for a, b in AB:
  if a == 0 and b == 0: 
    ze += 1
    continue
  if b == 0:
    na += 1
  elif a == 0:
    su += 1
  else:
    a, b = nasu(a, b)
    if a in R:
      if b in R[a]:
        R[a][b] += 1
      else:
        R[a][b] = 1
    else:
      R[a] = {}
      R[a][b] = 1

L = []
for i in R.keys():
  for j in R[i].keys():
    a, b = i, j
    x, y = -j, i
    if x < 0 and y < 0:
      x *= -1
      y *= -1
    t = R[i][j]
    if x not in R:
      L.append(pow(2, t, MOD))
      continue
    if y not in R[x]:
      L.append(pow(2, t, MOD))
      continue
    k = R[x][y]
    L.append((pow(2, t) + pow(2, k) - 1) % MOD)
    R[a][b] = 0
    R[x][y] = 0

L.append((pow(2, na) + pow(2, su) - 1) % MOD)

ans = 1
for i in L:
  ans = ans * i % MOD

ans = (ans + ze) % MOD

ans -= 1
if ans < 0:
  ans += MOD
print(ans)


