c = 0
s = f = ""
for i in input():
  s += i
  if s != f:
    c += 1
    s, f = "", s
print(c)