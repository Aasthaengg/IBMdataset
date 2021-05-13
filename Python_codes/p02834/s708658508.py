from collections import defaultdict

# def find_distances(edge_dict, node, distances):
#     for end in edge_dict[node]:
#         if distances[end] < 0:
#             distances[end] = distances[node] + 1
#             distances = find_distances(edge_dict, end, distances)

#     return distances


def find_distances(edge_dict, node, V):
    distances = [-1] * V
    stack = [(0, node)]

    while stack:
        dist, node = stack.pop()
        if distances[node] >= 0:
            continue

        distances[node] = dist
        for end in edge_dict[node]:
            stack.append((dist + 1, end))

    return distances

if __name__ == "__main__":
    V, T, A = map(int, input().split())
    T -= 1
    A -= 1
    edge_dict = defaultdict(list)

    for _ in range(V - 1):
        start, end = map(int, input().split())
        edge_dict[start - 1].append(end - 1)
        edge_dict[end - 1].append(start - 1)
    
    dist_T = [-1] * V
    dist_T[T] = 0
    dist_T = find_distances(edge_dict, T, V)

    dist_A = [-1] * V
    dist_A[A] = 0
    dist_A = find_distances(edge_dict, A, V)

    max_dist = 0
    for i in range(V):
        if dist_T[i] <= dist_A[i]:
            max_dist = max(max_dist, dist_A[i])
    
    print(max_dist - 1)
