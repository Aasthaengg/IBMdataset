n = int(input())
a = [int(x) for x in input().split()]

a.sort()
max_a = a[-1]
ans = 1

l, r = 0, n-1
while r-l > 1:
  key = (r+l)//2
  sub = a[key]
  judge = False
  if sub*2 >= max_a:
    judge = True
  for i in range(n):
    if judge:
      break
    if i == key:
      continue
    if a[i] <= sub*2:
      sub += a[i]
    if sub*2 >= max_a:
      judge = True
      break
  if judge:
    r = key
  else:
    l = key
key = r
if r == n-1 or r == 1:
  sub = a[l]
  judge = False
  if sub*2 >= max_a:
    judge = True
  for i in range(n):
    if judge:
      break
    if i == l:
      continue
    if a[i] <= sub*2:
      sub += a[i]
    if sub*2 >= max_a:
      judge = True
      break
  if judge:
    key = l
print(n-key)