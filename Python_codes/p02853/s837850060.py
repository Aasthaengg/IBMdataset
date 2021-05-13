x, y = map(int, input().split())
a = [300000, 200000, 100000]
ans = 0
if x <= 3: ans += a[x-1]
if y <= 3: ans += a[y-1]
if x == 1 and y == 1:
    ans += 400000
print(ans)