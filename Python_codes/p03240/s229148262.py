n = int(input())
lst = []
for i in range(n):
    xi, yi, hi = map(int, input().split())
    lst.append([xi, yi, hi])

lst.sort(reverse=True, key=lambda x: x[2])

for cx in range(101):
    for cy in range(101):
        h = -1
        for i in range(n):
            xi, yi, hi = lst[i]
            if h == -1:
                h = hi + abs(xi-cx) + abs(yi-cy)
                continue
            if hi != max(h - abs(xi-cx) - abs(yi-cy), 0):
                h = -1
                break
        if h != -1:
            print(cx, cy, h)
            exit()