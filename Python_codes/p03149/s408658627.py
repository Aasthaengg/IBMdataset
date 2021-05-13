a,b,c,d = map(str,input().split())
s = set()
s.add(a)
s.add(b)
s.add(c)
s.add(d)
if s == {"1","9","7","4"}:
  print("YES")
else:
  print("NO")