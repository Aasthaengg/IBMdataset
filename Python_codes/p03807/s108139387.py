n = int(input())
arr = list(map(int, input().split()))
tmp = 0
for i in range(n):
  if arr[i] % 2 == 1:
    tmp += 1
if tmp % 2 == 0:
  print('YES')
else:
  print('NO')