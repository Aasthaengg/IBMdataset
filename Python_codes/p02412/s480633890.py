def getWays(n, x):
  ways = []
  for i in xrange(1, n - 1):
    j = i + 1
    while j < n:
      # print "i = " + str(i) + ", j = " + str(j)
      remain = x - i - j
      if remain <= n and remain > j:
        list = [i, j, remain]
        ways.append(list)
      j+= 1
  return ways

while True:
  line = raw_input().split(" ")
  n = int(line[0])
  x = int(line[1])
  if n == 0 and x == 0:
    break
  else:
    print len(getWays(n, x))