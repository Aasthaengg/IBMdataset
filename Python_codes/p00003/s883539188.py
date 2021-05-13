n=input()
for _ in xrange(n):
  l=sorted(map(int, raw_input().split()))
  print "YES" if l[2]**2 == l[1]**2 + l[0]**2 else "NO"