N = int(input())
d = {0:0, 1:0}
A = map(int, input().split())
for a in A:
  d[a%2] += 1

if d[1] % 2 == 0:
  print('YES')
else:
  print('NO')