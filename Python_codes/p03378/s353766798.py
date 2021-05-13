a, b, c = map(int, input().split())
s = list(map(int, input().split()))
l, r = 0, 0
for i in s:
  if i < c:
    l += 1
  else:
    r += 1
print(min(l, r))
