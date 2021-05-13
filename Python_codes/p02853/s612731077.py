X, Y = map(int, input().split())
ans = 0

if X == Y == 1:
    ans = 400000

money = {3: 100000, 2: 200000, 1: 300000}
if X <= 3:
    ans += money[X]
if Y <= 3:
    ans += money[Y]

print(ans)
