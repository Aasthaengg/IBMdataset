x, y = map(int, input().split())

if x > 3:
    x = 0
if y > 3:
    y = 0
if x == 1 and y == 1:
    print(1000000)
else:
    print(100000 * (- x % 4) + 100000 * (- y % 4))