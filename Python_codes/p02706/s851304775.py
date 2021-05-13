n, m = map(int, input().split())
lst = [ int(i) for i in input().split() ]

if n - sum(lst) >= 0:
  print(n-sum(lst))
else:
  print(-1)
