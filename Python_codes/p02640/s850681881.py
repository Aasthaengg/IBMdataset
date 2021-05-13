X, Y = map(int,input().split())
ans = 0
for i in range(X+1):
  if 2 * i + 4 * (X - i) == Y:
    ans += 1

print( "Yes" if ans > 0 else "No")