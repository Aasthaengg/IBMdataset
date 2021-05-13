
a = list(map(int,input().split()))

a.sort()
cnt = 0

for i in range(1,3):
  cnt += a[i] - a[i-1]
print(cnt)
