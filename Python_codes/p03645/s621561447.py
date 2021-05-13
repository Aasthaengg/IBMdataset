n, m = map(int, input().split())
lst = [[] for i in range(n + 1)]
for i in range(m):
  tpl = tuple(map(int, input().split()))
  lst[tpl[0]].append(tpl[1])
for i in lst[1]:
  if n in lst[i]:
    print('POSSIBLE')
    exit()
print('IMPOSSIBLE')