N,x = map(int,input().split())
a = list(map(int,input().split()))
cnt = 0
for i in range(N):
  if i == 0:
    cnt += max(0,a[0] - x)
    a[0] -= max(0,a[0] - x)
  else:
    cnt += max(0,a[i] + a[i-1] - x)
    a[i] -= max(0,a[i] + a[i-1] - x)
print(cnt)