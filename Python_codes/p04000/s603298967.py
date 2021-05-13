from collections import Counter, defaultdict

h, w, n = map(int, input().split())
dic = defaultdict(int)
for _ in range(n):
    a, b = map(int, input().split())
    for y in range(a - 2, a + 1):
        for x in range(b - 2, b + 1):
            if 1 <= y <= h - 2 and 1 <= x <= w - 2:
                dic[(x, y)] += 1
counter = Counter(dic.values())
cntSum = (w - 2) * (h - 2)
counter[0] = cntSum - sum(counter.values())
for k in range(10):
    print(counter[k])