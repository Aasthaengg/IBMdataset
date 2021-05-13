list = [input() for i in range(2)]

s = list[0]
t = list[1]
lens = len(s)
lent = len(t)
if t.startswith(s)==True and lent-lens==1 and 1<=lens<=10:
  print("Yes")
else:
  print("No")