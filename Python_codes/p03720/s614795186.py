from collections import defaultdict
N, M = list(map(int, input().split()))
count = defaultdict(int)
for _ in range(M):
    a, b = list(map(int, input().split()))
    count[a] += 1
    count[b] += 1

for i in range(1, N + 1):
    print(count[i])