from collections import defaultdict

N, K = map(int, input().split())
d = defaultdict(int)

for _ in range(N):
    a, b = map(int, input().split())
    d[a] += b

n = 0
for i in range(10**5):
    n += d[i+1]
    if n >= K:
        print(i+1)
        exit()