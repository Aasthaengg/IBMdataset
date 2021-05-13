n= int(input())
a = list(map(int,input().split()))
xy = []
xyap = xy.append
ap = max(a)
a.remove(ap)
am = min(a)
a.remove(am)
for i in a:
  if i>0:
    xyap((am,i))
    am -= i
  else:
    xyap((ap,i))
    ap -= i
xyap((ap,am))
print(ap-am)
for i in xy:
  print(*i)