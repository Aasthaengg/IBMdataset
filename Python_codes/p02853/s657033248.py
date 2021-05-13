x, y = map(int, input().split())
ans = 0
money = [0, 3, 2, 1]

if x <= 3:
    ans += money[x]
if y <= 3:
    ans += money[y]

if x == 1 and y == 1:
    ans += 4

print(ans*10**5)