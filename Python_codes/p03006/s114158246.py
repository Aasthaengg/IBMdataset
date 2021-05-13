from collections import defaultdict

n = int(input())
x, y = [0] * n, [0] * n
data = defaultdict(int)
for i in range(n):
    x[i], y[i] = map(int, input().split())

if n == 1:
    print(1)
    exit()
for i in range(n):
    for j in range(n):
        if i != j:
            data[x[j] - x[i], y[j] - y[i]] += 1

print(n - max(data.values()))