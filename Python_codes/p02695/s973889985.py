import itertools

n,m,q = map(int,input().split())

a = [0] * q
b = [0] * q
c = [0] * q
d = [0] * q

for i in range(q):
  a1,b1,c1,d1 = map(int,input().split())
  a[i] = a1
  b[i] = b1
  c[i] = c1
  d[i] = d1

x = itertools.combinations_with_replacement(range(1,m+1),n)
tmp = 0
ans = 0
for xi in x:
  tmp = 0

  for i in range(q):
    if xi[b[i]-1] - xi[a[i]-1] == c[i]:
      tmp += d[i]
  ans = max(ans,tmp)

print(ans)