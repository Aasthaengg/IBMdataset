N, = map(int, raw_input().split())
a = map(int, raw_input().split())
mi = 0
ma = abs(a[0])
for i in range(1,N):
  if abs(a[i])>ma:
    ma = abs(a[i])
    mi = i
print 2*N
if a[mi]>=0:
  print mi+1, N
  print mi+1, N
  for i in range(N-1):
    print N, i+1
    print N, N
else:
  print mi+1, 1
  print mi+1, 1
  for i in range(N-1, 0, -1):
    print 1, i+1
    print 1, 1