A, B, C = map(int, input().split())
ans = A*B*C
if (A*B*C)%2==0:
  print(0)
else:
  print(ans//max([A,B,C]))
