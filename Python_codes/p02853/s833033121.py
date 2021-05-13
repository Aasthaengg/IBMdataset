x,y = map(int,input().split())
c = 0
for i in [x,y]:
  if i < 4:
    c += [3*10**5,2*10**5,10**5][i-1]
if x == y == 1:
  c += 4*10**5
print(c)