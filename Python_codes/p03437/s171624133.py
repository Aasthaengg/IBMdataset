X, Y = map(int, input().split())
if X % Y == 0:
  ans = -1
elif Y % X == 0:
  ans = X * (Y//X + 1)
else:
  ans = X
if ans > 10**18:
  ans = -1
if X == 1 and Y != 1:
  ans = Y + 1
print(ans)