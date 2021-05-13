n, m = list(map(int, input().split()))
a = [0] * m
b = [0] * m
for i in range(m):
    a[i], b[i] = list(map(int, input().split()))

road = [0] * n

for i in range(m):
    road[a[i] - 1] += 1
    road[b[i] - 1] += 1

for i in range(n):
    print(road[i])