n,m = map(int,input().split())
energy = sorted([tuple(map(int,input().split())) for _ in range(n)])
ret = 0
ind = 0
while(m):
  a,b = energy[ind]
  if b > m:
    ret += a * m
    m = 0
  else:
    ret += a * b
    m -= b
  ind += 1
print(ret)