a,b = map(int,input().split())
point = 0
point += max(a,b)

if max(a,b) == a:
  point += max(a-1,b)
  print(point)
else:
  point += max(a,b-1)
  print(point)
