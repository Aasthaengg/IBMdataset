n,m,k = map(int,input().split())

able_set = set()
for ni in range(n+1):
  base = ni * m
  for mi in range(m+1):
    black = base - ni*mi + (n-ni)*mi    
    able_set.add(black)    
    
if k in able_set:
  print('Yes')
else:
  print('No')