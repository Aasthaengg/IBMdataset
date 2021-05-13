import copy
n = int(input())
a = [int(input()) for _ in range(n)]
b = copy.deepcopy(a)
a.sort(reverse=True)
for v in b:
  if v==a[0]:
    print(a[1])
  else:
    print(a[0])