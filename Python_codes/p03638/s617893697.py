h,w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
now = 0
for i in range(h):
  ans = []
  res = w
  while a[now] < res:
    ans += [now+1 for i in range(a[now])]
    res -= a[now]
    now += 1
  else:
    ans += [now+1 for i in range(res)]
    a[now] -= res
  if i % 2:
    ans.reverse()
  print(*ans)