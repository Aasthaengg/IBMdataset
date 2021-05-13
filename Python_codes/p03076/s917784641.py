lst = [input() for i in range(5)]
d = [int(num) for num in lst]
lst_one = [int(list(i)[-1]) for i in lst]
if lst_one.count(0) == len(lst_one):
  print(sum(d))
else:
  if lst_one.count(0) == 0:
    idx = lst_one.index(min(lst_one))
  else:
    no_zero = [i for i in lst_one if i != 0]
    m = min(no_zero)
    idx = lst_one.index(m)

  x = d[idx]
  del d[idx]

  for i in range(len(d)):
    if d[i] % 10 != 0:
      d[i] = 10*(int((d[i]/10))+1)
    else:
      continue
  print(sum(d) + x)