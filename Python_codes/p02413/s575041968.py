l, c = map(int, input().split())
tbl = [[] for _ in range(l)]
li_sum = [0 for _ in range(c+1)]

for i in range(l):
  a = input()
  tbl[i] = list(map(int, a.split()))
  print(a, end='')
  print(' ', sum(tbl[i]), sep = '')

  for j in range(c):
    li_sum[j] += tbl[i][j]
  li_sum[c] += sum(tbl[i])

print(' '.join(map(str, li_sum)))
