_ = input()
edges = list(map(int, input().split()))
max_edge = max(edges)
print('Yes' if max_edge < sum(edges) - max_edge else 'No')