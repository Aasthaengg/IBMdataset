import collections
s = input()
c = collections.Counter(s)

if c["a"] == c["b"] == c["c"]:
  print("YES")
  exit()
if c["a"]+1 == c["b"] == c["c"]:
  print("YES")
  exit()
if c["a"]-1 == c["b"] == c["c"]:
  print("YES")
  exit()
if c["a"] == c["b"]+1 == c["c"]:
  print("YES")
  exit()
if c["a"] == c["b"]-1 == c["c"]:
  print("YES")
  exit()
if c["a"] == c["b"] == c["c"]+1:
  print("YES")
  exit()
if c["a"] == c["b"] == c["c"]-1:
  print("YES")
  exit()
else:
  print("NO")