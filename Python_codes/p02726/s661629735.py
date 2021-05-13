N, X, Y = map(int, input().split())
X -= 1
Y -= 1
edge = []
for i in range(N):
    edge.append([])
    if i != 0:
        edge[i].append(i - 1)
    if i != N-1:
        edge[i].append(i + 1)
edge[X].append(Y)
edge[Y].append(X)

answer = [0] * (N - 1)
for i in range(N):
    queue = []
    for e in edge[i]:
        queue.append(e)
    counter = 0
    d = [N + 10] * N
    d[i] = 0
    # i is start
    while counter < len(queue):
        node = queue[counter]
        min_dist = N + 10
        for e in edge[node]:
            if d[e] < min_dist:
                min_dist = d[e]
            if d[e] == N + 10:
                queue.append(e)
        d[node] = min_dist + 1
        counter += 1
    for i in d:
        answer[i] += 1
for a in answer[1:]:
    print(a//2)
print('0')