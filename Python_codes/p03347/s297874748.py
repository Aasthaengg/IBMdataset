n = int(input())
a = [int(input()) for _ in range(n)]
if a[0] != 0:
  print(-1)
  exit(0)
cnt = 0
cur = 0
for i in range(n-1,-1,-1):
  if cur > a[i]:
    print(-1)
    exit(0)
  if cur < a[i]:
    cur = a[i]
    cnt += a[i]
  if cur > 0:
    cur -= 1
print(cnt)