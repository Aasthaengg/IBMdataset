n = int(input())
a = list(map(int,input().split()))
if(1 in a):
  ans = 0
  jud = 0
  f = 1
  for i in range(n):
    if(a[i]!=f):
      ans += 1
    else:
      f += 1
  print(ans)
else:
  print(-1)
