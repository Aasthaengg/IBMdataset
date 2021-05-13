from collections import Counter

N, M = map(int, input().split())
c = Counter()

for _ in range(M):
    a, b = map(int, input().split())
    c[a] += 1
    c[b] += 1

for i in range(1, N + 1):
    print(c[i])
