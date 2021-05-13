H, W, N = map(int, raw_input().split())
p = set()
for i in range(N):
  a, b = map(int, raw_input().split())
  p.add((a,b))
r = [0]*10
c = set()
for a, b in p:
  for y0 in range(a-2, a+1):
    for x0 in range(b-2, b+1):
      if x0<1 or x0+2>W or y0<1 or y0+2>H or (y0,x0) in c:
        continue
      c.add((y0,x0))
      s = 0
      for y in range(y0, y0+3):
        for x in range(x0, x0+3):
          if (y,x) in p:
            s += 1
      r[s] += 1
print (H-2)*(W-2)-sum(r[1:10])
for ri in r[1:10]:
  print ri