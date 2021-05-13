k = int(raw_input())
a = map(int,raw_input().split(" "))

if a[-1] != 2:
  print "-1"
  exit(0)

r = [2,3]
ainv = a[::-1]

for now in ainv[1:]:
  lower = (r[0]/now)*now
  if lower < r[0]:
    lower += now
  upper = (r[1]/now)*now

  q = [lower,upper]

  if q[0] > r[1]:
    print "-1"
    exit(0)
  #print r,q
  q[1] = q[1] + now - 1
  r = q

print "%d %d" % (r[0],r[1])
