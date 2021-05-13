import bisect

n = int(input())
a = list(map(int,input().split()))
a.sort()
amax = a[-1]

if amax//2 in set(a):
  print(amax,amax//2)
else:
  ind = bisect.bisect_left(a,amax//2)
  MIN = min(abs(a[ind]-(amax//2)),abs(a[ind-1]-(amax//2)))
  if amax == 100 and a[ind] == 100:
    print(100,0)
    exit()
  
  if MIN == abs(a[ind]-(amax//2)):
    print(amax,a[ind])
  else:
    print(amax,a[ind-1])