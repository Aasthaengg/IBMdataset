n,a,b = map(int,input().split())
maxx = max(a,b)
minn = min(a,b)
bet = maxx - minn - 1
if bet % 2 == 0:
  print("Borys")
else:
  print("Alice")