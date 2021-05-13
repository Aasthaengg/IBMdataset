h, w, n = map(int, input().split())
cnts = [0] * 10
cnts[0] = (h-2)*(w-2)

points = dict()
for _ in range(n):
    a, b = map(lambda x: int(x)-1, input().split())
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            ai, bj = a+i, b+j
            if 1 <= ai < h-1 and 1 <= bj < w-1:
                ab = (a+i, b+j)
                points.setdefault(ab, 0)
                cnts[points[ab]] -= 1
                points[ab] += 1
                cnts[points[ab]] += 1
for c in cnts:
    print(c)
