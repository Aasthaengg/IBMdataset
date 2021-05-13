n = int(input())
ans = 0
ansc = 0
def dc(m):
  cnt = 0
  x = m
  while (True):
    if x%2 == 0:
      cnt += 1
      x = x//2
    else:
      break
  return cnt
for i in range(1,n+1):
  c = dc(i)
  if c > ansc:
    ans = i
    ansc = c
if n == 1:
  print(1)
else:
  print(ans)