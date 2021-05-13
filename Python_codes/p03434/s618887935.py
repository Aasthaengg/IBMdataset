N = int(input())
if N == 1:
  print(input())
else:
  A = 0
  B = 0
  a = list(map(int,input().split()))
  a.sort()
  a.reverse()
  for i in range(N):
    if i % 2 == 0:
      A += a[i]
    else:
      B += a[i]
  print(A - B)