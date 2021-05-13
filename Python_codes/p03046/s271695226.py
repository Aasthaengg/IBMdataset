M, K = map(int,input().split())
if M==1:
  if K!=0:
    print(-1)
  else:
    print(0,0,1,1)
elif K>=2**M:
  print(-1)
else:
  b = [i for i in range(K)] + [i for i in range(K+1,2**M)]
  c = b[::-1]
  ans = b+[K]+c+[K]
  print(*ans)