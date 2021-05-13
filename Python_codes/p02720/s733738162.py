def expand(x):
  s = x[0]
  if (s == '0'):
    e = ['0', '1']
  elif (s == '9'):
    e = ['8', '9']
  else:
    e = [str(int(s) + (i-1)) for i in range(3)]
  y = [i+x for i in e]
  return y


Y      = [str(i) for i in range(10)]
result = Y.copy()

for _ in range(10):
  tmp = []
  for i in Y:
    tmp += expand(i)
  result.extend(tmp)
  Y = tmp
  
iY = set(map(int, result))
iY = sorted(list(iY))

X = int(input())
print(iY[X])