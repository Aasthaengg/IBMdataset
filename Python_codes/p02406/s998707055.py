n = int(raw_input())
print "",
for i in range(1, n+1):
  if i % 3 == 0:
    print "%d" % i,
  else:
    z = i
    while 1:
      if z % 10 == 3:
        print "%d" % i,
        break
      z /= 10
      if z == 0:
        break