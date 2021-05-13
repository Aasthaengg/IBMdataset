def calc():
  H,W,M = map(int, input().split())
  s = []
  hcount = [0]*H
  wcount = [0]*W
  for m in range(M):
    h,w = map(int, input().split())
    h = h - 1
    w = w - 1
    hcount[h] = hcount[h] + 1
    wcount[w] = wcount[w] + 1
    s.append((h,w))
  hmax = max(hcount)
  wmax = max(wcount)
  hmode = [h for h, x in enumerate(hcount) if x == hmax]
  wmode = [w for w, y in enumerate(wcount) if y == wmax]
  s = tuple(s)
  S = set(s)
  for h in hmode:
    for w in wmode:
      if ((h,w) not in S):
        return hmax + wmax
  return hmax + wmax - 1
  
if __name__ == '__main__':
    print(calc())