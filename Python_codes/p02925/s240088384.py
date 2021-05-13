#16:07
n = int(input())
raw = []
for _ in range(n):
  raw.append(list(map(lambda x: int(x)-1, input().split())))
cnt = [0 for _ in range(n)]
tmp = [0 for _ in range(n)]
now = [i for i in range(n)]
ans = 0
while now:
  ans += 1
  last = now
  now = []
  for x in last:
    tmp[x] = 0
  for x in last:
    try:
      y = raw[x][cnt[x]]
      if tmp[x] == tmp[y] == 0 and x == raw[y][cnt[y]]:
        cnt[x] += 1
        cnt[y] += 1
        tmp[x] = 1
        tmp[y] = 1
        now.append(x)
        now.append(y)
    except:
      pass
  #print(now)
if cnt == [n-1 for _ in range(n)]:
  print(ans-1)
else:
  print(-1)