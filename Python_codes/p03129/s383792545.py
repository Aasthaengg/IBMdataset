n,k = map(int, input().split())
od = [i for i in range(1,n+1)]
odn = od[::2]
if len(odn) >=k:
  print('YES')
else:
  print('NO')