N, K = map(int, input().split())

total = (N - 1) * (N - 2) // 2
if K > total:
    print(-1)
else:
    edges = []
    for k in range(2, N + 1):
        edges.append([1, k])

    res = total - K
    cnt = 0
    for u in range(2, N + 1):
        if cnt == res:
            break
    
        for v in range(u + 1, N + 1):
            edges.append([u, v])
            cnt += 1

            if cnt == res:
                break

    print(len(edges))
    for v in edges:
        print(*v)