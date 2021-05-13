from collections import Counter

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
XY.sort()
diff = []
for i in range(N):
    xi, yi = XY[i]
    for j in range(i+1, N):
        xj, yj = XY[j]
        diff.append((xj-xi, yj-yi))
c = Counter(diff)
print(N-max(c.values()) if c else N)