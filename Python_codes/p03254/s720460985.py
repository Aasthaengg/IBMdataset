N,x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

A = sum(a)
if x > A:
  print(N-1)

else:
  cnt = 0
  for i in range(N):
    if x >= a[i]:
      x -=a[i]
      cnt += 1
  print(cnt)