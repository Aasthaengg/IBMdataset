n,m,k = map(int,input().split())
if k <= m:
  print("delicious")
else:
  if m < k <= m + n:
    print("safe")
  else:
    print("dangerous")