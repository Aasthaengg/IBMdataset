l = list(map(int, input().split()))
if(l[0] %2 == 0 or l[1] %2==0 or l[2]%2==0):
  print(0)
else:
  a = l.pop(l.index(min(l)))
  b = l.pop(l.index(min(l)))
  print(a*b)