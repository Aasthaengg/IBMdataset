n, m, p = map(int, input().split())
abcs = [list(map(int, input().split())) for _ in range(m)]
distance = [-1000000 * n] * (n + 1)

distance[1] = 0
reachable1 = set([1])
reachableN = set([n])
for _ in range(n + 1):
    for a, b, c in abcs:
        if distance[b] < distance[a] + c - p:
            distance[b] = distance[a] + c - p
        # 枝刈りが必要                                                                                                                                                                                                                
        if a in reachable1:
            reachable1.add(b)
        if b in reachableN:
            reachableN.add(a)

for a, b, c in abcs:
    if (distance[b] < distance[a] + c - p) and (a in reachable1) and (b in reachableN):
        print(-1)
        exit(0)

print(max(distance[n], 0))