tmp = raw_input().split()
a = int(tmp[0])
b = int(tmp[1])

if a > b:
  print "a > b"
elif a == b:
  print "a == b"
else:
  print "a < b"