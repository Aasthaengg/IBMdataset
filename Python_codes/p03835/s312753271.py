k,s = map (int ,input ().split ())
x = 0
y = 0
p = 0
while x <= k:
  while y <= k:
    if x+y > s:
      break
    z = s-(x+y)
    if 0 <= z <= k:
      p += 1
    y += 1
  x += 1
  y = 0
print (p)