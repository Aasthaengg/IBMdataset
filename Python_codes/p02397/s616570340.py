while True:
  x,y = map(int,raw_input().split())
  if x == y == 0:
    break
  print min(x,y), max(x,y)