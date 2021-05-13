n = int(raw_input())
for x in range(n) :
  edges = map(int, raw_input().split())
  a = min(edges); edges.remove(a)
  b = min(edges); edges.remove(b)
  c = edges[0]

  if a**2 + b**2 == c**2 :
    print "YES"
  else :
    print "NO"