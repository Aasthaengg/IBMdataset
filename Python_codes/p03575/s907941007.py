from collections import deque
def main():
    n, m = list(map(int, input().split()))
    G = [[] for _ in range(n)]
    L = []
    for _ in range(m):
        a, b = list(map(lambda x: int(x) - 1, input().split()))
        G[a].append(b)
        G[b].append(a)
        L.append(set([a, b]))
    ans = 0
    for l in L:
        stack = deque([0, ])
        visited = [False] * n
        while stack:
            x = stack.popleft()
            if visited[x]:
                continue
            visited[x] = True
            for dx in G[x]:
                if set([x, dx]) == l:
                    continue
                if not visited[dx]:
                    stack.append(dx)
        if not all(visited):
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
