a,b = map(str,input().split())
d = {'H':'D','D':'H'}
if a=='H':
  print(b)
else:
  print(d[b])