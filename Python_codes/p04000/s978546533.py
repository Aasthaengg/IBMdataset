from collections import defaultdict

h, w, n = map(int, input().split())
d = defaultdict(int)
for i in range(n):
    a, b = map(int, input().split())
    for k in range(3):
        if 1 <= a - k <= h - 2:
            for l in range(3):
                if 1 <= b - l <= w - 2:
                    x = (a - k, b - l)
                    d[x] += 1
ans = [0] * 10
for v in d.values():
    ans[v] += 1
ans[0] = (h - 2) * (w - 2) - sum(ans[1:])
for i in range(10):
    print(ans[i])
