k = int(input())
prev_lunlun = list(range(1, 10))
lunlun = prev_lunlun[:]

while len(lunlun) < k:
    next_lunlun = []
    for x in prev_lunlun:
        r = x % 10
        y = x * 10 + r
        next_lunlun.append(y)
        if r != 9:
            next_lunlun.append(y+1)
        if r != 0:
            next_lunlun.append(y-1)
    lunlun += next_lunlun
    prev_lunlun = next_lunlun
lunlun.sort()
print(lunlun[k-1])