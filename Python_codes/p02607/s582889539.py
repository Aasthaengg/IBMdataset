n, *a = map(int, open(0).read().split())
cnt = 0
for i in range(0, n, 2):
  if a[i] % 2 == 1 :
    cnt += 1
print(cnt)