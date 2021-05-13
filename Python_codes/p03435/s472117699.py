lst = []
for i in range(3):
  l = list(map(int, input().split()))
  lst.append(l)
for i in range(1, 3):
  diff = lst[i][0] - lst[0][0]
  for j in range(3):
    lst[i][j] -= diff
  if lst[i] != lst[0]:
    print('No')
    exit()
print('Yes')