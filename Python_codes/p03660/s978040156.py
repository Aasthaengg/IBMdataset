import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import defaultdict, deque

    n = int(readline())
    edge = defaultdict(list)

    for _ in range(n - 1):
        a, b = map(int, readline().split())
        a, b = a - 1, b - 1
        edge[a].append(b)
        edge[b].append(a)

    que1 = deque()
    que1.append(0)
    que2 = deque()
    que2.append(n - 1)

    df = [-1] * n
    ds = [-1] * n
    df[0] = 0
    ds[n - 1] = 0

    while que1:
        u = que1.popleft()
        for v in edge[u]:
            if df[v] == -1:
                que1.append(v)
                df[v] = df[u] + 1

    while que2:
        u = que2.popleft()
        for v in edge[u]:
            if ds[v] == -1:
                que2.append(v)
                ds[v] = ds[u] + 1

    cf, cs = 0, 0
    for f, s in zip(df, ds):
        if f <= s:
            cf += 1
        else:
            cs += 1

    if cf > cs:
        print("Fennec")
    else:
        print("Snuke")


if __name__ == '__main__':
    main()
