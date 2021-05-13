n,*a=map(int,open(0).read().split())
if len(a)==len(set(a)):
  print("YES")
else:
  print("NO")