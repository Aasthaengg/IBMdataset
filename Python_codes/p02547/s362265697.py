n = int(input())
d1 = [0] * n
d2 = [0] * n
for i in range(n):
  d1[i], d2[i] = (map(int, input().split()))
cnt = 0

for i in range(n):
  if d1[i] == d2[i]:
    cnt += 1
  else:
    cnt = 0
  if cnt >= 3:
    break

if cnt >= 3:
  print("Yes")
else:
  print("No")