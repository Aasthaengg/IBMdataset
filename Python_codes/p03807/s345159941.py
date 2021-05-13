N = int(input())
if len([int(x) for x in input().strip().split() if int(x) % 2]) % 2:
  print('NO')
else:
  print('YES')