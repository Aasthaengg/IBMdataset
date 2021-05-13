ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n,r = nm()

if n<10:
  print(r+(10-n)*100)
else:
  print(r)