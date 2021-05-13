from collections import defaultdict

d = defaultdict(int)
N = int(input())
for _ in range(N):
    s = str(input())
    d[s] += 1
M = int(input())
for _ in range(M):
    t = str(input())
    d[t] -= 1

print(max(0, max(d.values())))