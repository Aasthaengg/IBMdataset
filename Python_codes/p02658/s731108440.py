n=int(input())
a=[int(x) for x in input().split()]
if 0 in a:
  print(0)
else:
  b=1
  for i in range(n):
    b*=a[i]
    if b>10**18:
      print(-1)
      exit()
  print(b)