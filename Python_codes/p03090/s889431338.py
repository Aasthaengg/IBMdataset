n = int(input())

l = list(range(1, n+1))
s = sum(l)
graph = []
graph_set = set()
cnt = 0

if n % 2 == 0:
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i + j == n + 1:
                continue
            elif i == j:
                continue
            else:
                if (i, j) not in graph_set:
                    graph.append([i, j])
                    graph_set.add((i, j))
                    graph_set.add((j, i))
                    cnt += 1

else:
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i + j == n:
                continue
            elif i == j:
                continue
            else:
                if (i, j) not in graph_set:
                    graph.append([i, j])
                    graph_set.add((i, j))
                    graph_set.add((j, i))
                    cnt += 1

print(cnt)
for i, j in graph:
    print(i, j)