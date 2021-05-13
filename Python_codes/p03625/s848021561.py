from collections import Counter

input()
lengths = tuple(map(int, input().split(' ')))
counter = Counter(lengths)

edges = []

for length in sorted(counter.keys(), reverse=True):
    if counter[length] >= 4:
        edges.append(length)
        edges.append(length)
    elif counter[length] >= 2:
        edges.append(length)

    if len(edges) >= 2:
        break

edges.append(0)
edges.append(0)

edges.sort(reverse=True)

print(edges[0] * edges[1])
