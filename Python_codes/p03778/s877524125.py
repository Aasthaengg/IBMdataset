import sys

w, a, b = list(map(int, input().split()))
temp = 0

if a > b:
  temp = a
  a = b
  b = temp
if a == b or a+w == b or w == b:
  ans = 0
  print(ans)
  sys.exit()
else:
  if b > a+w:
    ans = abs(b-(a+w))
  else:
    ans = abs((a+w)-b)

print(ans)