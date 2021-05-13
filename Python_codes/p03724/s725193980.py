from collections import Counter

N, M = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(M)]

ctr = Counter()
for a, b in X:
    ctr[a] += 1
    ctr[b] += 1

if all(v % 2 == 0 for v in ctr.values()):
    print("YES")
else:
    print("NO")
