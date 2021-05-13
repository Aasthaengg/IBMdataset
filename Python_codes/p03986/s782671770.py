x = input()
res = [x[0]]
for i in x[1:]:
  if i == 'S':
    res += [i]
  elif not res:
    res += [i]
  else:
    if res[-1] == 'S':
      res.pop()
    else:
      res += [i]
print(len(res))
