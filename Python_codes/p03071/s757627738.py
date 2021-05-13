X, Y = map(int, input().split())
ans = 0
if X < Y:
    ans = Y
    Y -= 1
else:
    ans = X
    X -= 1

if X < Y:
    ans += Y
else:
    ans += X

print(ans)
