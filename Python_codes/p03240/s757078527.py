n = int(input())
l = []
for i in range(n):
    xyh = list(map(int, input().split()))
    l.append(xyh)
    if xyh[2]:
        x, y, h = xyh
for i in range(101):
    for j in range(101):
        k = h + abs(i - x) + abs(j - y)
        if all(h == max(k - abs(i - x) - abs(j - y), 0) for x, y, h in l):
            print(i, j, k)