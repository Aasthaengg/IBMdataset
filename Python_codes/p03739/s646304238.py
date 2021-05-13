n = int(input())
a = list(map(int,input().split()))
can = []
ans = 0
now = 0
for i in range(n):
  now += a[i]
  if i % 2 == 0:
    if now <= 0:
      ans += 1 - now
      now = 1
  else:
    if now >= 0:
      ans += 1 + now
      now = -1
can.append(ans)
ans = 0
now = 0
for i in range(n):
  now += a[i]
  if i % 2 == 1:
    if now <= 0:
      ans += 1 - now
      now = 1
  else:
    if now >= 0:
      ans += 1 + now
      now = -1
can.append(ans)
print(min(can))