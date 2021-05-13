n = int(input())
MOD = 1000000007

ans = 1
x_sardines = []
ver_sardines = []
hor_sardines  = []
zero_sardines  = []

for _ in range(n):
  ai, bi = map(int, input().split())
  if ai == 0 and bi != 0:
    ver_sardines.append((ai, bi))
  elif ai != 0 and bi == 0:
    hor_sardines.append((ai, bi))
  elif ai == 0 and bi == 0:
    zero_sardines.append((ai, bi))
  elif bi / ai > 0:
    x_sardines.append((ai, bi, 1))
  elif bi / ai < 0:
    x_sardines.append((- 1 * bi, ai, -1))

x_sardines.sort(key = lambda x: x[1] / x[0])

if len(x_sardines) > 0:
  pai, pbi, ps = x_sardines[0]
  p = 1 if ps == 1 else 0
  n = 1 if ps == -1 else 0
  for i, (ai, bi, s) in enumerate(x_sardines[1:]):
    if pai * bi - pbi * ai != 0:
      ans *= pow(2, p, MOD) + pow(2, n, MOD) - 1
      ans %= MOD
      p = 0
      n = 0
      
    if s == 1:
      p += 1
    elif s == -1:
      n += 1
    pai, pbi, ps = ai, bi, s

  ans *= pow(2, p, MOD) + pow(2, n, MOD) - 1
  ans %= MOD
  
v = len(ver_sardines)
h = len(hor_sardines)
ans *= pow(2, v, MOD) + pow(2, h, MOD) - 1
ans %= MOD

z = len(zero_sardines)
ans += z
ans -= 1
ans %= MOD

print(ans)


