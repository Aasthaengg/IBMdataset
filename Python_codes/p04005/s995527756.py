A, B, C = map(int,input().split())

if (A * B * C) % 2 == 0:
  ans = 0
else:
  ans = min(A*B,B*C,C*A)
print(ans)