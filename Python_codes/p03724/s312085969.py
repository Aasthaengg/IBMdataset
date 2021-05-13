import sys

N, M = map(int, sys.stdin.readline().strip().split())

paths = []
count = {}
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    paths.append((a, b))

    if a not in count:
        count[a] = 0
    if b not in count:
        count[b] = 0
    count[a] += 1
    count[b] += 1

for key, c in count.items():
    if c % 2 != 0:
        print("NO")
        break
else:
    print("YES")