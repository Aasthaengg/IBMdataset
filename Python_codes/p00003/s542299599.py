n = int(raw_input())
for _ in xrange(n):
  ls = sorted(map(int, raw_input().split()))
  if ls[2]**2 == ls[0]**2+ls[1]**2: print "YES"
  else: print "NO"