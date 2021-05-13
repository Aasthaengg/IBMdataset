ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

k,x = nm()

if 500*k>=x:
  print('Yes')
else:
  print('No')