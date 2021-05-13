from collections import defaultdict, Counter

H, W, N = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

ctr = defaultdict(int)
for a, b in X:
    for k in range(3):
        for l in range(3):
            if 1 <= a - k <= H - 2 and 1 <= b - l <= W - 2:
                ctr[(a - k, b - l)] += 1

d = Counter(ctr.values())
for i in range(10):
    if i == 0:
        print((H - 2) * (W - 2) - sum(d.values()))
    else:
        print(d[i])
