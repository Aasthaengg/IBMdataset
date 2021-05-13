while 1:
  l = [int(x) for x in list(input())]
  if 0 in l and len(l) == 1: break
  print(sum(l))
