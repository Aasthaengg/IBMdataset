def main():
    import sys
    input = sys.stdin.buffer.readline
    N = int(input())
    c = [[int(i) for i in input().split()] for j in range(N)]
    from collections import defaultdict
    edge = defaultdict(set)
    deg = defaultdict(int)
    for i, A in enumerate(c, start=1):
        for j in range(N-2):
            if i < A[j]:
                if i < A[j+1]:
                    edge[i*N+A[j]].add(i*N+A[j+1])
                    deg[i*N+A[j+1]] += 1
                else:
                    edge[i*N+A[j]].add(A[j+1]*N+i)
                    deg[A[j+1]*N+i] += 1
            else:
                if i < A[j+1]:
                    edge[A[j]*N+i].add(i*N+A[j+1])
                    deg[i*N+A[j+1]] += 1
                else:
                    edge[A[j]*N+i].add(A[j+1]*N+i)
                    deg[A[j+1]*N+i] += 1
    from collections import deque
    que = deque()
    dist = defaultdict(int)
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            # print(i, j, i*N+j)
            if deg[i*N+j] == 0:
                que.append(i*N+j)  # root
                dist[i*N+j] = 1
    while que:
        u = que.popleft()
        for v in edge[u]:
            deg[v] -= 1
            dist[v] = max(dist[v], dist[u] + 1)
            if deg[v] == 0:
                que.append(v)

    if any(deg.values()):
        # 閉路検出
        print(-1)
    else:
        print(max(dist.values()))


if __name__ == '__main__':
    main()
