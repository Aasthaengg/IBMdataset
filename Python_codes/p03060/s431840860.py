n = raw_input()
vis = map(int, raw_input().split(' '))
cis = map(int, raw_input().split(' '))
r= 0
for c,v in zip(cis, vis):
  r += max(0,v - c)
print r
