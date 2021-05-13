a,b=map(int,input().split())

if min(a, b) > 0 and max(a, b) < 10:
  print(a*b)
else:
  print(-1)