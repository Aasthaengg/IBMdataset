s = int(input())
c = set([s])

i = 1
while 1:

  if s % 2 == 0:
    s //= 2
  else:
    s = s*3+1

  i += 1

  if s in c:
    break
  else:
    c.add(s)

print(i)