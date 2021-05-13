from collections import Counter
n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]
v = []
for i in range(n):
    for j in range(n):
        if i == j: continue
        x, y = xy[j]
        px, py = xy[i]
        v.append((x-px, y-py))
num = Counter(v).most_common(1)[0][1] if v else 0
print(n - num)
