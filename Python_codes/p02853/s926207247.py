
X, Y = map(int,input().split())

ans = max(4-X,0)* 100000 + max(4-Y,0)* 100000
if (X == Y) *  (Y== 1):
  ans += 400000
print(ans)