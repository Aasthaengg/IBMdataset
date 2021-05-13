from collections import deque
N, M = map(int, input().split())
table = []
for i in range(N):
    table.append([])
for i in range(M):
    Ai, Bi = map(int, input().split())
    table[Ai - 1].append(Bi - 1)
    table[Bi - 1].append(Ai - 1)

cost = [1000000] * N
queue = [0]
counter = 0
cost[0] = 0
answer = [-1] * N
answer[0] = 0
while counter < len(queue):
    current = queue[counter]
    counter += 1

    for n in table[current]:
        if cost[current] + 1 < cost[n]:
            cost[n] = cost[current] + 1
            answer[n] = current
            queue.append(n)
print('Yes')
for a in map(lambda x: x + 1, answer[1:]):
    print(a)

