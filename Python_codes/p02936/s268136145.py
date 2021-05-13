from collections import deque, defaultdict


def main():
    n, q = [int(e) for e in input().split()]
    AB = [[int(e) for e in input().split()] for i in range(n - 1)]
    PX = [[int(e) for e in input().split()] for i in range(q)]

    G = defaultdict(set)
    for a, b in AB:
        G[a].add(b)
        G[b].add(a)

    Ans = [0] * (n + 1)
    for p, x in PX:
        Ans[p] += x

    Q = deque([1])
    Visited = [False] * (n + 1)
    Visited[1] = True
    while len(Q) > 0:
        v = Q.popleft()
        for vc in G[v]:
            if Visited[vc]:
                continue

            Ans[vc] += Ans[v]
            Q.append(vc)
            Visited[vc] = True

    print(*Ans[1:])


if __name__ == '__main__':
    main()
