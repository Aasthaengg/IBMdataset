from collections import Counter
n, k = map(int, input().split())

c = Counter()
for _ in range(n):
    a, b = map(int, input().split())
    c[a] += b
c = sorted(c.items(), key=lambda x: x[0])

for i, v in c:
    k -= v
    if k <= 0:
        print(i)
        exit()