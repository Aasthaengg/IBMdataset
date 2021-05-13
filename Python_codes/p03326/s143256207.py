n, m = [int(i) for i in input().split()]
xyz = [[int(i) for i in input().split()] for _ in range(n)]

ans = 0
a = [0]*3
for a[0] in range(-1, 2, 2):
    for a[1] in range(-1, 2, 2):
        for a[2] in range(-1, 2, 2):
            d = list(map(lambda x: sum([i * j for i, j in zip(a, x)]), xyz))
            d.sort(reverse=1)

            ans = max(ans, sum(d[:m]))
print(ans)
