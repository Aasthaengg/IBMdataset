n,m = list(map(int,input().split()))
count = 0

if 2*n < m:
  count += n
  m = m - 2*n
  n = 0  
  count += m//4
else:
  count += m//2


print(count)

