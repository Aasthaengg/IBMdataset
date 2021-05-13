n, t = map(int, input().split())

alist = list(map(int, input().split()))

lowest = float('INF')

gain = 0

repeat = 0

for al in alist:
    if al < lowest:
        lowest = al
        continue
    else:
        if al - lowest == gain:
            repeat += 1
            continue
        if al - lowest > gain:
            gain = al - lowest
            repeat = 0
            continue

print(repeat + 1)