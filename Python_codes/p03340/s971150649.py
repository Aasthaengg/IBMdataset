n = int(input())
a = list(map(int, input().split()))
start, end = 0, 1
now = a[0]
ans = 0
while end < n:
  NEXT = a[end]
  if now + NEXT == now ^ NEXT:
    now += NEXT
    end += 1
  else:
    LEN = end - start
    ans += LEN
    now -= a[start]
    start = start + 1
LEN = end - start
ans += LEN * (LEN+1) // 2
print(ans)