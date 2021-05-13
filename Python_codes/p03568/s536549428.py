import  itertools as it

N,*A = map(int,open(0).read().split())

cnt = 0
for Z in it.product(range(3),repeat=N):
  t = 1
  for z,a in zip(Z,A):
    t*=(a+z-1)
  if t%2 == 0:
    cnt+=1
print(cnt)