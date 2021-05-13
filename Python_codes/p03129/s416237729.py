n,k = input().split()
n = int(n)
k = int(k)
for l in range(k):
  l = 2*l +1
  c = l
if c <= n:
  print('YES')
else:
  print('NO')