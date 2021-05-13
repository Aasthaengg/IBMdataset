n, k = map(int, input().split())
a = list(map(int, input().split()))

m = n-k
if m>0:
  if m%(k-1)==0:
    print(m//(k-1) + 1)
  else:
    print(m//(k-1) + 2)
else:
  print(m//(k-1) + 1)