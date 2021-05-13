n = int(input())
r = list(map(int,input().split()))

m = max(r)
r.pop(r.index(max(r)))

if sum(r) > m:
  print('Yes')
else:
  print('No')