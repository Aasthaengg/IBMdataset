n, x = map(int, input().split())
l = list(map(int, input().split()))
count = 1
d = 0
for li in l:
  d += li
  if d > x:
    break
  count += 1
print(count)