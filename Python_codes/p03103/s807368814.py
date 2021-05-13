from operator import itemgetter
n, m = map(int, input().split())
lst = []
for i in range(n):
  lst.append(tuple(map(int, input().split())))
lst.sort(key=itemgetter(0))
res = 0
for i in range(n):
  if lst[i][1] <= m:
    m -= lst[i][1]
    res += (lst[i][0] * lst[i][1])
  else:
    res += (lst[i][0] * m)
    break
print(res)