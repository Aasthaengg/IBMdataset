s = list(input())
t = list(input())
ss = "".join(sorted(s))
tt = "".join(sorted(t, reverse=True))
flag = False
if ss < tt:
  print("Yes")
else:
  print("No")