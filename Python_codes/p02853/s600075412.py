x, y = map(int, input().split())
ans = 0
m = [0, 300000, 200000, 100000]
if 1 <= x <= 3:
  ans += m[x]
if 1 <= y <= 3:
  ans += m[y]
if x == y == 1:
  ans += 400000
print(ans)