x, y = map(int, input().split())
prize = max(0, 4 - x) + max(0, 4 - y)
if x == y == 1:
  prize += 4
print(prize * 100000)