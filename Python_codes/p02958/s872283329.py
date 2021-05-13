N = int(input())
p = list(map(int, input().split()))

M = [i for i in range(1, N+1, 1)]

count = 0
for i in range(N):
  if p[i] != M[i]:
    count += 1
if count == 2 or count == 0:
  print('YES')
else:
  print('NO')