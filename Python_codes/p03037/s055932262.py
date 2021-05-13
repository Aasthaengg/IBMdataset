n,m = map(int,input().split())
Low = []
Right = []
for i in range(m):
  l,r = map(int,input().split())
  Low.append(l)
  Right.append(r)
if min(Right) < max(Low):
  print(0)
else:
  print(min(Right)- max(Low) + 1)