n = int(input())
a = list(map(int, input().split()))
o = 0
for i in range(n):
  if a[i] % 2 == 1: o += 1
if o % 2 == 0: print('YES')
else: print('NO')