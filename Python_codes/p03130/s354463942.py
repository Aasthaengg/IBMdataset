a, b = map(int, raw_input().split())
c, d = map(int, raw_input().split())
e, f = map(int, raw_input().split())
r = a^b^c^d^e^f
bad = 1^2^3^4
if r == bad:
  print "NO"
else:
  print "YES"