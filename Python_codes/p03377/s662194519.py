ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

a,b,x=nm()

if a+b>=x and a<=x:
  print('YES')
else:
  print('NO')