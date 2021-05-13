from collections import Counter, defaultdict

ans = defaultdict(lambda: 0)
h, w, n = map(int, input().split())
for _ in range(n):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    for a_i in range(a - 2, a + 1):
        for b_i in range(b - 2, b + 1):
            if (0 <= a_i < h - 2) & (0 <= b_i < w - 2):
                ans[(a_i, b_i)] += 1

k = Counter(ans.values())
print((h - 2) * (w - 2) - sum(k.values()))
for i in range(1, 10):
    if i in k.keys():
        print(k[i])
    else:
        print(0)