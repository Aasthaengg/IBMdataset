x, y = map(int, input().split())
prize = [300000, 200000, 100000]
total = 0
if x <= 3:
    total += prize[x-1]
if y <= 3:
    total += prize[y-1]
if x == y == 1:
    total += 400000
print(total)