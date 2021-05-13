from collections import defaultdict
N, M = map(int, input().split())
d = defaultdict(int)
for _ in range(M):
    a, b = map(int, input().split())
    d[a] += 1
    d[b] += 1
for k, v in d.items():
    if v % 2 != 0:
        print("NO")
        exit()
print("YES")