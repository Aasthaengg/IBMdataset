X, Y = map(int, input().split())
ans = -1
if X % Y :
  ans = X * (Y - 1)
print(ans)
