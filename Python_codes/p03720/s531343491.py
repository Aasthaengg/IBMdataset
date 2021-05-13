from collections import defaultdict

N, M = map(int, input().split())
d = defaultdict(int)

for _ in range(M):
    a, b = map(int, input().split())
    d[a] += 1
    d[b] += 1

for i in range(N):
    print(d[i+1])