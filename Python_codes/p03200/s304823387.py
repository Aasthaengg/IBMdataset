s = list(input())
b = 0
c = 0
for a in s:
  if a == 'B':
    b += 1
  else:
    c += b
print(c)