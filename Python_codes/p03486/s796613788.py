a = [input() for i in range(2)]

sp = "".join(sorted(list(a[0])))
tmp = list(a[1])
tmp.sort()
tmp.reverse()
tp = "".join(tmp)

if sp < tp:
  print("Yes")
else:
  print("No")
