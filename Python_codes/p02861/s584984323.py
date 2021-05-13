import itertools

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]


dist = 0
f = 0
for v in itertools.permutations(l, n):
    f += 1
    for i in range(1, n):
        x1, y1 = v[i-1]
        x2, y2 = v[i]
        dist += ((x1-x2)**2 + (y1-y2)**2)**0.5
res = round(dist/f, 10)
print(res)