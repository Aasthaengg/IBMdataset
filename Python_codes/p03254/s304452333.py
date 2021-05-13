N,x = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
if sum(a) < x:
  print(N-1)
  exit()
cnt = 0
su = 0
for i in range(N):
  if su + a[i] <= x:
    su += a[i]
    cnt += 1
  else:
    break
print(cnt)