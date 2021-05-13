import collections

N = int(input())

if N == 1:
    print(1)
    exit()

x_y = []
for _ in range(N):
    x_y.append(list(map(int, input().split())))

x_y.sort(key=lambda x: (x[0], x[1]))
pq_cand = []
for i in range(N):
    for j in range(i + 1, N):
        pq_cand.append((x_y[j][0] - x_y[i][0], x_y[j][1] - x_y[i][1]))

pqc = collections.Counter(pq_cand)
_, x = max(pqc.items(), key=lambda x: x[1])
print(N - 1 - x + 1)
