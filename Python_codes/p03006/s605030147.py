from collections import Counter


N = int(input())
M = [tuple(map(int, input().split())) for _ in range(N)]
Map = []
if N == 1:
    print(1)
    exit()
for i in range(N):
    x1, y1 = M[i]
    for j in range(N):
        if i == j:
            continue
        x2, y2 = M[j]
        Map.append((x2 - x1, y2 - y1))
MapC = Counter(Map)
print(N - MapC.most_common(1)[0][1])



