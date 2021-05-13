n,m = map( int,input().split() )
a = [ list(map(int,input().split())) for _ in range(n)]

a.sort()

c = 0
for i in range(n):
  x = min(m,a[i][1])
  c += x * a[i][0]
  m -= x
  if m == 0 :
    break

print(c)