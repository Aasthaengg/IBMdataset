n = int(input())
r = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
  r[i] = [r[i][0] - r[i][1], r[i][0] + r[i][1]]
r.sort(key = lambda x:x[1])
#print(r)
cur = -1001001001
ans = 0
for i in range(n):
  if cur <= r[i][0]:
    ans += 1
    cur = r[i][1]
print(ans)