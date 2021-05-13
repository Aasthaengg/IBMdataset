#16:40
m,k = map(int,input().split())
if k >= 2**m:
  print(-1)
elif m == 1 and k == 1:
  print(-1)
elif m == 1 and k == 0:
  print(1,1,0,0)
else:
  a = []
  for i in range(2**m):
    if i != k:
      a.append(i)
  b = list(reversed(a))
  ans = b + [k] + a + [k]
  #print(ans)
  print(' '.join((list(map(str,ans)))))