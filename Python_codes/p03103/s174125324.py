N, M = map(int, input().split())
l = []
for i in range(N):
  l.append(list(map(int, input().split())))
  
l.sort()
cnt, ans = 0, 0
for i in range(N):
  if cnt+l[i][1] <= M:
    cnt += l[i][1]
    ans += l[i][0] * l[i][1]
  else:
    ans += (M-cnt) * l[i][0]
    break
print(ans)