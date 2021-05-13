def solve():
  n = int(input())
  s = [input() for _ in range(n)]
  l = []
  for si in s:
      lparen = rparen = 0
      for c in si:
          if c == '(':
              lparen += 1
          else:
              if lparen > 0:
                  lparen -= 1
              else:
                  rparen += 1
      l.append((rparen, lparen))
  inc = []
  dec = []
  for p, q in l:
      if p < q:
          inc.append((p, q))
      else:
          dec.append((p, q))
  inc.sort()
  k = 0
  for p, q in inc:
      if k < p:
          print('No')
          return
      k = k - p + q
  dec.sort(key=lambda x: x[1])
  t = 0
  for p, q in dec:
      if t < q:
          print('No')
          return
      t = t - q + p
  if k == t:
      print('Yes')
  else:
      print('No')
  return


solve()
