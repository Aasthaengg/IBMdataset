import math

while True:
  n = int(raw_input())
  if n == 0:
    break
  s = map(float, raw_input().split(" "))

  sum = 0
  for i in xrange(n):
    sum += s[i]
  a = sum / n

  temp = 0
  for i in xrange(n):
    temp += (s[i] - a) ** 2
  temp = math.pow(temp / n, 0.5)

  print "{0:.6f}".format(temp)