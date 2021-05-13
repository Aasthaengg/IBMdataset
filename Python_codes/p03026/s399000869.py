def msol19_d():
    n = int(input())
    graph = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(lambda x: int(x)-1, input().split())
        graph[a].append(b)
        graph[b].append(a)
    C = sorted(map(int, input().split()), reverse=True)

    score = sum(C[1:])
    label = [-1]*n
    from collections import deque
    que = deque([0])
    idx = 0
    while que:
        u = que.popleft()
        label[u] = C[idx]
        idx += 1
        for v in graph[u]:
            if label[v] != -1: continue
            que.append(v)
    print(score)
    print(*label, sep=' ')

if __name__ == '__main__':
    msol19_d()