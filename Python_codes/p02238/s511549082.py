from sys import setrecursionlimit

setrecursionlimit(10 ** 9)

n = int(input())

graph = []

for _ in range(n):
    tmp = list(map(int, input().split()))

    if tmp[1] == 0:
        graph.append([])
        continue
    else:
        graph.append(list(map(lambda x: x - 1, tmp[2: tmp[1] + 2])))

d = [-1] * n
f = [-1] * n

time = 1


def dfs(x):
    if d[x] != -1:
        return

    global time

    d[x] = time
    time += 1

    for n in graph[x]:
        dfs(n)

    f[x] = time
    time += 1


for i in range(n):
    dfs(i)

for i in range(n):
    print(i + 1, d[i], f[i])

