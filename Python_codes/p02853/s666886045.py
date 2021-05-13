X, Y = map(int,input().split())

ans = 0

if X == 3:
  ans = ans + 100000
elif X == 2:
  ans = ans + 200000
elif X == 1:
  ans = ans + 300000

if Y == 3:
  ans = ans + 100000
elif Y== 2:
  ans = ans + 200000
elif Y == 1:
  ans = ans + 300000

if (X == 1)and(Y==1):
  ans = ans+ 400000
print(ans)