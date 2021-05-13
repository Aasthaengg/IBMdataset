import sys
n, k = map(int, input().split())
if k > (n-1)*(n-2)//2:
  print(-1)
  sys.exit()

key = 0
ans = []
for i in range(2, n+1):
  if k == 0:
    for j in range(1, i):
      ans.append((i, j))
  else:
    ans.append((1, i))
    if k >= key:
      k -= key
      key += 1
    else:
      key -= k
      for j in range(2, 2+key):
        ans.append((i, j))
      k = 0

print(len(ans))
for value in ans:
  print(*value)