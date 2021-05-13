import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import Counter, deque, defaultdict

    n, k, l = map(int, readline().split())

    edge1 = defaultdict(list)

    for _ in range(k):
        p, q = map(int, readline().split())
        edge1[p - 1].append(q - 1)
        edge1[q - 1].append(p - 1)

    a = [-1] * n
    que = deque()

    for i in range(n):
        if a[i] == -1:
            que.append(i)
            a[i] = i
            while que:
                cur = que.popleft()
                for nx in edge1[cur]:
                    if a[nx] == -1:
                        a[nx] = i
                        que.append(nx)

    edge2 = defaultdict(list)

    for _ in range(l):
        r, s = map(int, readline().split())
        edge2[r - 1].append(s - 1)
        edge2[s - 1].append(r - 1)

    b = [-1] * n
    que = deque()

    for i in range(n):
        if b[i] == -1:
            que.append(i)
            b[i] = i
            while que:
                cur = que.popleft()
                for nx in edge2[cur]:
                    if b[nx] == -1:
                        b[nx] = i
                        que.append(nx)

    c = Counter()
    for i in range(n):
        c[(a[i], b[i])] += 1

    res = [0] * n
    for i in range(n):
        res[i] = c[(a[i], b[i])]

    print(*res)


if __name__ == '__main__':
    main()
