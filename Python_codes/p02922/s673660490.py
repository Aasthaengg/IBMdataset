a,b = map(int, input().split())
c = 1
ans = 0
if b == 1:
  ans = 0
else:
  for i in range(21):
    c = c-1 + a
    if c >= b:
      ans = i + 1
      break
print(ans)