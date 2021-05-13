N,*A = map(int,open(0).read().split())

cnt = 0

e = 0
o = 0
for a in A:
  if a%2 ==0:
    e+=1
  else:
    o+=1

print(3**N -2**e)
