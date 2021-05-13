n = int(raw_input())
a = map(int,raw_input().split(" "))

ans = []
aa = sorted(a)

if aa[0] < 0 and aa[n-1] > 0:
  bt = aa[0]
  up = aa[n-1]
  if abs(bt) > abs(up):
    r = a.index(bt)
    for x in range(n):
      if x != r:
        a[x] += bt
        ans.append([r+1,x+1])
  else:
    r = a.index(up)
    for x in range(n):
      if x != r:
        a[x] += up
        ans.append([r+1,x+1])

aa = sorted(a)

if aa[0] == aa[n-1]:
  print 0
  exit()

if aa[0] >= 0: # all plus!
  for x in range(n-1):
    a[x+1] += a[x]
    ans.append([x+1,x+2])
elif aa[n-1] <= 0: # all minus!
  for x in range(n-2,-1,-1):
    a[x] += a[x+1]
    ans.append([x+2,x+1])

print len(ans)
for q in ans:
  print "%d %d" % (q[0],q[1])

