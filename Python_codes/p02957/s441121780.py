A, B = map(int, input().split())
ans = A + B

if ans % 2 == 0:
  ans = int(ans//2)
  print(ans)
else:
  print('IMPOSSIBLE')