n, k = map(int, input().split())
a = list(map(int, input().split()))

l , r = 0, max(a)

def ok(L):
  cnt = 0
  for i in a:
    cnt += i // L
    if i % L == 0:
      cnt -= 1
  return cnt <= k

while r - l > 1:
  mid = (r + l) //2

  if ok(mid):
    r = mid
  else:
    l = mid

print(r)