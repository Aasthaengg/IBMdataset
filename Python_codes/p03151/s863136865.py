n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
if sum(a) < sum(b):
  print(-1)
  exit()
cnt = 0
ans = 0
d = []
for i in range(n):
  if a[i] < b[i]:
    ans += 1
    cnt += b[i] - a[i]
  else:
    d.append(a[i] - b[i])
if ans == 0:
  print(ans)
  exit()
d.sort(reverse=True)
for x in d:
  ans += 1
  cnt -= x
  if cnt <= 0:
    print(ans)
    break