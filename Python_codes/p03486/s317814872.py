import sys
s = input()
t = input()

s = list(s)
s.sort()
s2 = "".join(s)

t = list(t)
t.sort(reverse=True)
t2 = "".join(t)

if s2 < t2:
  print("Yes")
else:
  print("No")