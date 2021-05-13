
d = None
f = None


def dfs(g, cur, time):
    global d, f
    d[cur] = time
    for next in g[cur]:
        if d[next] == 0:
            time = dfs(g, next, time+1)
    f[cur] = time + 1
    return time + 1


def main():
    global d, f
    n = int(input())
    g = [[] for _ in range(n)]
    d = [0 for _ in range(n)]
    f = [0 for _ in range(n)]
    for _ in range(n):
        inp = list(map(int, input().split()))
        m = inp[0] - 1
        k = inp[1]
        for i in range(k):
            g[m].append(inp[i+2] - 1)
    time = 1
    for i in range(n):
        if d[i] == 0:
            time = dfs(g, i, time) + 1
    for i in range(n):
        print(i+1, d[i], f[i])


if __name__ == '__main__':
    main()

