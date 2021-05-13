a,m = map(int,input().split())
hl = [tuple(map(int,input().split())) for i in range(m)]
hl.sort()
l,r = -1,a+1
c = 0
for i in hl:
  l = i[0]
  r = min(r,i[1])
  if l >= r:
    c += 1
    r = i[1]
print(c+1)