n, k = map(int, input().split())

edges = [(0, i) for i in range(1, n)]
cnt = (n-1) * (n-2) // 2

if k == cnt:
    print(n-1)
    for u, v in edges:
        print(u+1, v+1)
    exit()

for i in range(1, n-1):
    for j in range(i+1, n):
        edges.append((i, j))
        cnt -= 1
        if cnt == k:
            print(len(edges))
            for u, v in edges:
                print(u+1, v+1)
            exit()

print(-1)
