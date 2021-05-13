s = input()
q = int(input())
s1 = ""
s2 = ""
c = 1
for i in range(q):
  a = input()
  if " " in a:
    l = list(a.split())
    c2 = 3-2*int(l[1])
    if c*c2 == 1:
      s1 = s1 + l[2]
    else:
      s2 = s2 + l[2]
  else:
    c = -c
s = s1[::-1] + s + s2
if c == 1:
  print(s)
else:
  print(s[::-1])