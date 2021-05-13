l = []
o = ["+", "-", "*"]
for i in input().split():
  if i in o:
    t = eval("{0}{1}{2}".format(l[-2], i, l[-1]))
    l.pop(-1)
    l[-1] = t
  else: l += [int(i)]
print(*l)
