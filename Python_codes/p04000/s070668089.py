from collections import defaultdict, Counter
H, W, N = map(int, input().split())
D = defaultdict(int)

for i in range(N):
    a, b = map(int, input().split())
    for y in range(3):
        for x in range(3):
            if 0 < a - y <= H - 2 and 0 < b - x <= W - 2:
                D[(a - y, b - x)] += 1

C = Counter(D.values())
SUM = sum(C.values())

print((H - 2) * (W - 2) - SUM)
for i in range(1, 10):
    print(C[i])
