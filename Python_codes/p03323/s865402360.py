ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

a,b = nm()

if a>8 or b>8:
  print(':(')
else:
  print('Yay!')