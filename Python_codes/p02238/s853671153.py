def main():
    n = int(input())
    _next, state, d, f = [], [False] * n, [0] * n, [0] * n
    for _ in range(n):
        u, k, *v = map(lambda s: int(s) - 1, input().split())
        _next.append(sorted(v, reverse=True))
    stack = []
    time = 0

    while True:
        for i in range(n):
            if not state[i]:
                stack.append(i)
                state[i] = True
                time += 1
                d[i] = time
                break
        if not stack:
            break
        while stack:
            u = stack[-1]
            if _next[u]:
                v = _next[u].pop()
                if not state[v]:
                    state[v] = True
                    time += 1
                    d[v] = time
                    stack.append(v)
            else:
                time += 1
                f[u] = time
                stack.pop()

    for i in range(n):
        print(i + 1, d[i], f[i])


if __name__ == '__main__':
    main()

