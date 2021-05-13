n = int(input())
wf = []
for _ in range(n):
  wf.append(list(map(int,input().split())))
cnt = [[0 for _ in range(n)] for _ in range(n)]
for k in range(n):
  for i in range(n):
    for j in range(n):
      if wf[i][j] > wf[i][k] + wf[k][j]:
        print(-1)
        exit()
      elif wf[i][j] == wf[i][k] + wf[k][j]:
        cnt[i][j] += 1
#print(cnt)
ans = 0
for i in range(n):
  for j in range(n):
    if cnt[i][j] <= 2:
      ans += wf[i][j]
print(ans//2)