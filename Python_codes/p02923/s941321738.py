n = int(input())
h = [int(x.strip()) for x in input().split()]
i, ch, ans = 0, 0, 0
while i < n-1:
  if h[i] >= h[i+1]:
    ch += 1
  elif h[i] < h[i+1]:
    if ch > ans:
      ans = ch
    ch = 0
  i += 1
if ch > ans:
  ans = ch
print(ans)