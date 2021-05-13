def getFinal(initial, m, h):
  for i in xrange(m):
    temp = initial[:h[i]]
    # print "temp = " + temp
    initial = initial[h[i]:] + temp
    # print initial
  return initial

while True:
  initial = raw_input()
  if initial == "-":
    break
  m = int(raw_input())
  h = []
  for i in xrange(m):
    h.append(int(raw_input()))

  # line = "*******************"
  # print line
  # print initial
  # print m
  # print h
  # print line

  print getFinal(initial, m, h)