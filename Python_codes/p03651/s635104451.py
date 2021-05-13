n,k = map(int, input().split())
a = [int(s) for s in input().split()]

if k > max(a):
  print('IMPOSSIBLE')
elif min(a) == 1 or k in a:
  print('POSSIBLE')
else:
  divmax = min(a)
  divval = 1
  for div in range(divmax):
    for x in a:
      if x % (div+1) != 0:
        break
    else:
      divval = div + 1
  if k % divval == 0:
    print('POSSIBLE')
  else:
    print('IMPOSSIBLE')