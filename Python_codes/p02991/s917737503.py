n,m = map(int,input().split())
pst = [[] for _ in range(n)]
for _ in range(m):
  a,b = map(int,input().split())
  a -= 1
  b -= 1
  pst[a].append(b)
s,t = map(int,input().split())
s -= 1
t -= 1
cnt = [[0,0,0] for _ in range(n)]
cnt[s][0] = 1
now = [s]
time = 0
while now:
  time += 1
  last = now
  now = []
  for x in last:
    for y in pst[x]:
      if cnt[y][time%3] == 0:
        cnt[y][time%3] = 1
        now.append(y)
  #print(time,cnt,now)
  if cnt[t][0] == 1:
    print(time//3)
    break
else:
  print(-1)