import heapq
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if sum(a) < sum(b) :
  print(-1)
else :
  ans = 0
  lack = 0
  que = [0]
  heapq.heapify(que)
  for i in range(n) :
    a[i] -= b[i]
    if a[i] < 0 :
      ans += 1
      lack -= a[i]
    else :
      heapq.heappush(que,-a[i])
  while lack > 0 :
    m = heapq.heappop(que)
    lack += m
    ans += 1
  print(ans)