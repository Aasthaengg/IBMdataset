ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n,m=sorted(nm())

if n==1 and m==1:
  print(1)
elif n==1:
  print(m-2)
else:
  print((n-2)*(m-2))