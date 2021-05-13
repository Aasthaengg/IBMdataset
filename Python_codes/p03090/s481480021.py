N = int(input())
edges = []
for i in range(1, N // 2 + 1):
    j = N - i + 1 - N % 2
    for k in range(1, N+1):
        if k == i or k == j:
            continue
        if i < k:
            edges.append((i, k))
        if j < k:
            edges.append((j, k))
print(len(edges))
for a, b in edges:
    print(a, b)