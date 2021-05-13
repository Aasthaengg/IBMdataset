a=input()
s = {a[0],a[1],a[2],a[3]}
if len(s) == 2:
  b = s.pop()
  flag1 = a.count(b)
  c = s.pop()
  flag2 = a.count(c)
  if flag1 ==2 and flag2 == 2:
    print("Yes")
  else:
    print("No")
else:
  print("No")