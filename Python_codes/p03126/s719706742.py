n,m = map(int, input().split())
l = dict()
for i in range(1,m+1):
  l[i] = 0

for i in range(n):
  x = list(map(int, input().split()))
  k = x[0]
  for j in x[1:]:
    l[j] += 1

cnt = 0
for k,v in l.items():
  if v==n:
    cnt += 1
print(cnt)