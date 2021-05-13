def main():
    from collections import deque
    import sys
    input = sys.stdin.readline

    N = int(input())
    Graph = tuple(set() for _ in range(N))
    for _ in range(N - 1):
        a, b = (int(x) - 1 for x in input().split())
        Graph[a].add(b)
        Graph[b].add(a)

    Fennec = [-1] * N
    Snuke = [-1] * N

    def bfs(start, arr):
        arr[start] = 0
        dq = deque()
        dq.append(start)
        while dq:
            v = dq.popleft()
            d = arr[v]
            for u in Graph[v]:
                if ~arr[u]:
                    continue
                arr[u] = d + 1
                dq.append(u)

    bfs(start=0, arr=Fennec)
    bfs(start=N - 1, arr=Snuke)

    cnt_f = sum(1 for f, s in zip(Fennec, Snuke) if f <= s)
    cnt_s = N - cnt_f

    print('Fennec' if cnt_f > cnt_s else 'Snuke')


if __name__ == '__main__':
    main()
