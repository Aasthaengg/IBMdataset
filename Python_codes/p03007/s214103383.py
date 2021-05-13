from heapq import heapify,heappop,heappush
n = int(input())
a = list(map(int,input().split()))
if max(a) > 0 and min(a) < 0:
  hp = []
  hn = []
  heapify(hp)
  heapify(hn)
  ans = 0
  for i in range(n):
    if a[i] >= 0:
      heappush(hp,a[i])
      ans += a[i]
    else:
      ans -= a[i]
      heappush(hn,a[i])
  print(ans)
  while hp and hn:
    p = heappop(hp)
    q = heappop(hn)
    if hn:
      print(p,q)
      heappush(hp,p-q)
    elif hp:
      print(q,p)
      heappush(hn,q-p)
    else:
      print(p,q)
elif min(a) >= 0:
  ans = sum(a)-2*min(a)
  print(ans)
  heapify(a)
  while a:
    p = heappop(a)
    if a:
      q = heappop(a)
      if a:
        print(p,q)
        heappush(a,p-q)
      else:
        print(q,p)
    else:
      break
elif max(a) <= 0:
  ans = -sum(a)+2*max(a)
  a = [-a[i] for i in range(n)]
  heapify(a)
  print(ans)
  while a:
    p = heappop(a)
    if a:
      q = heappop(a)
      if a:
        print(-p,-q)
        heappush(a,p-q)
      else:
        print(-p,-q)
    else:
      break