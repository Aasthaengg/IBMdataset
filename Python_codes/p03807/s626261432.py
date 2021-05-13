n = int(input())
l = list(map(int, input().split()))
t = 0
for i in range(n):
  if l[i]%2 == 1:
    t += 1
if t%2 == 1:
  print('NO')
else:
  print('YES')