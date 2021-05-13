h, n = map(int, input().split())

a = [0] * n
b = [0] * n

for i in range(n):
    a[i], b[i] = map(int, input().split())

magic = [float("inf")] * (h + 1)
magic[0] = 0

for i in range(n):
    for j in range(0, h + 1):
        if j + a[i] <= h:
            magic[j + a[i]] = min(magic[j + a[i]], magic[j] + b[i])
        else:
            magic[h] = min(magic[h], magic[j] + b[i])

print(magic[h])