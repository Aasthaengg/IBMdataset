n, r = map(int,input().split())
if (n >= 10):
  print(r)
else:
  sa = 100*(10 - n)
  print(r + sa)
