def main():
  N = int(input())
  xyh = [[int(_) for _ in input().split()] for __ in range(N)]
  for cx in range(0, 101):
    for cy in range(0, 101):
      H = set()
      for x, y, h in xyh:
        if h == 0:
          continue
        H.add(abs(cx - x) + abs(cy - y) + h)
      if len(H) == 1:
        ok = True
        hh = list(H)[0]
        for x, y, h in xyh:
          if h == 0:
            if max(hh - abs(cx - x) - abs(cy - y), 0) == 0:
              continue
            else:
              ok = False
        if ok:
          print(cx, cy, *H)
          break
    else:
      continue
    break
  return

if __name__ == '__main__':
  main()
