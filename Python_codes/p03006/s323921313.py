from collections import Counter

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

if N == 1:
    print(1)
    exit()

xy.sort(key=lambda x: x[1])
xy.sort(key=lambda x: x[0])

ans = N
diff = []

for i in range(N-1):
    for j in range(i+1, N):
        diff.append((xy[j][0]-xy[i][0], xy[j][1]-xy[i][1]))

c = Counter(diff)
print(N - c.most_common()[0][1])