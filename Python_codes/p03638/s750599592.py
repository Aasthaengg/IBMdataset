h, w = map(int, input().split())
n = int(input())
a = [int(x) for x in input().split()]

ans = [[0]*w for _ in range(h)]

key = 0
for i in range(h):
  if i%2 == 0:
    for j in range(w):
      ans[i][j] = key+1
      a[key] -= 1
      if not a[key]:
        key += 1
  else:
    for j in range(w-1, -1, -1):
      ans[i][j] = key+1
      a[key] -= 1
      if not a[key]:
        key += 1

for i in range(h):
  print(*ans[i])