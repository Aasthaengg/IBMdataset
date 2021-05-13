a, b, c = map(int, input().split())
k = int(input())
for i in range(k):
  if a < b < c:
    break
  elif a >= c  or b >= c:
    c *= 2
  else:
    b *= 2
if a < b < c:
  ans = 'Yes'
else:
  ans = 'No'
print(ans)