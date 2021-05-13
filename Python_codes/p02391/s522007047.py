res = raw_input().split()
res[0] = int(res[0])
res[1] = int(res[1])

if res[0] == res[1]:
  print "a == b"
elif res[0] < res[1]:
  print "a < b"
else:
  print "a > b"