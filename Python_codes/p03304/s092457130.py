n, m, d = map(int,input().split(' '))
c = 2
if d == 0:
  c = 1
print(c * (n-d)/n/n*(m-1))
