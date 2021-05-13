n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
for k in range(n):
  for i in range(n-1):
    for j in range(i+1,n):
      if a[i][j] > a[i][k] + a[k][j]:
        print(-1); exit(0)

for i in range(n-1):
  for j in range(i+1,n):
    for k in range(n):
      if k == i or k == j: continue
      elif a[i][j] == a[i][k] + a[k][j]:
        cnt += a[i][j]
        break
tot = sum(sum(x) for x in a)//2
print(tot-cnt)