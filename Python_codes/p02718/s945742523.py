n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
cnt = 0
sum_ = sum(a)
for ai in a:
  if ai >= 1 / (4 * m) * sum_:
    cnt += 1
if cnt >= m:
  print('Yes')
else:
  print('No')