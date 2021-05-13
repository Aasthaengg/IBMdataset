arr = []
while True:
  value = int(raw_input())
  if value != 0:
    arr.append(value)
  else:
    break

count = 1
for x in arr:
  print "Case %s: %s" % (count, x)
  count += 1