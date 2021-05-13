A, B, C = map(int, input().split())
ans = 0
if A%2 == 0 or B%2 == 0 or C%2 ==0:
  ans = 0
else:
  ans = min([A*B,B*C,C*A])
print(ans)