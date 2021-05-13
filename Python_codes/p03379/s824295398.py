import copy
n = int(input())
lst = list(map(int, input().split()))
clst = sorted(copy.deepcopy(lst))
lmed = clst[n // 2 - 1]
rmed = clst[n // 2]
for i in range(n):
  if lst[i] <= lmed:
    print(rmed)
  else:
    print(lmed)