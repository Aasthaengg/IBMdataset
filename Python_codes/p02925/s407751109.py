#16:07
n = int(input())
raw = []
for _ in range(n):
  raw.append(list(map(lambda x: int(x)-1, input().split())))
cnt = [0 for _ in range(n)]
now = []
for i in range(n):
  j = raw[i][cnt[i]]
  if i < j and i == raw[j][cnt[j]]:
    now.append(i)
    now.append(j)
ans = 0
while now:
  ans += 1
  last = now
  now = []
  for x in last:
    cnt[x] += 1
    if cnt[x] < n-1:
      y = raw[x][cnt[x]]
      if x == raw[y][cnt[y]]:
        now.append(x)
        now.append(y)
  #print(now)
if cnt == [n-1 for _ in range(n)]:
  print(ans)
else:
  print(-1)
