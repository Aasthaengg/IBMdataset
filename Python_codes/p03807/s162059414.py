n = int(input())
A = list(map(int, input().split()))
num_odd = 0
for a in A:
  if a % 2 == 1:
    num_odd += 1
if num_odd % 2 == 0:
  print('YES')
else:
  print('NO')