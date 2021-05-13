from collections import defaultdict

N, K = map(int, input().split())
d = defaultdict(int)
for i in range(N):
    a, b = map(int, input().split())
    d[a] += b
for k in sorted(d.keys()):
    K -= d[k]
    if K <= 0:
        print(k)
        exit()
