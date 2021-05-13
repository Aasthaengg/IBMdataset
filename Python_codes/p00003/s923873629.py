def to_i(e):
  return int(e)

n = int(raw_input().rstrip())

for i in range(n):
  a = sorted(map(to_i, raw_input().rstrip().split(" ")))
  if a[0]*a[0]+a[1]*a[1] == a[2]*a[2]:
    print "YES"
  else:
    print "NO"