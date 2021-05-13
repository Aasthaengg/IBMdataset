import bisect

n, *lst = map(int, open(0).read().split())
alst = sorted(lst[:n])
blst = lst[n:2*n]
clst = sorted(lst[2*n:])
res = 0
for i in blst:
  a = bisect.bisect_left(alst, i)
  c = n - bisect.bisect_right(clst, i)
  res += a * c
print(res)