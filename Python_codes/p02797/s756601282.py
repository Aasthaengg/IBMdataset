n,k,s = map(int,input().split())
if s!=10**9:
  l = [s for i in range(k)]
  l1 = [10**9 for i in range(n-k)]
  print(*(l+l1))
  exit()
else:
  l = [s for i in range(k)]
  l1 = [1 for i in range(n-k)]
  print(*(l+l1))