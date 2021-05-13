n,m = map(int,input().split())
a = list(map(int,input().split()))

total = sum(a)

a.sort(reverse=True)
a_m = a[:m]
if a_m[-1] >= total / (4 * m):
  print('Yes')
else:
  print('No')