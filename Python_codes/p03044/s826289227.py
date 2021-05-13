def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b, c = (int(i) for i in input().split())
        G[a-1].append((b-1, c % 2))
        G[b-1].append((a-1, c % 2))

    color = [-1]*N

    def dfs(s):
        seen = [False]*N
        stack = [s]
        seen[s] = True
        color[0] = 0
        while stack:
            v = stack.pop()
            for u, dist in G[v]:
                if seen[u]:
                    continue
                if dist == 1:
                    color[u] = color[v] ^ 1
                else:
                    color[u] = color[v]
                stack.append(u)
                seen[u] = True

    dfs(0)
    print(*color, sep="\n")


if __name__ == '__main__':
    main()
