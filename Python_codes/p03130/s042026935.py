a = [[]]*3
for i in range(3):
  a[i] = list(map(int, input().split()))

cnt = 0
for i in range(1,5):
  tmp = 0
  for j in range(3):
    tmp += a[j].count(i) 
  if tmp == 2:
    cnt += 1

if cnt == 2:
  print("YES")
else:
  print("NO")