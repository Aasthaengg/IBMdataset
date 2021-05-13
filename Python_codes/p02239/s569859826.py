n = int(input())
al = [list(map(lambda x: int(x) - 1, input().split()))[2:] for _ in range(n)]
queue = [0]
d = [-1] * n
d[0] = 0
while len(queue) > 0:
    u = queue.pop(0)
    for v in al[u]:
        if d[v] == -1:
            d[v] = d[u] + 1
            queue.append(v)
for i, x in enumerate(d):
    print('{} {}'.format(i + 1, x))


