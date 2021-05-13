N,D = (int(i) for i in input().split())

tmp = D*2 + 1

ans = N//tmp

if N%tmp == 0:
  print(ans)
else:
  print(ans+1)
