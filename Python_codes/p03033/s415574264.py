from heapq import heappop, heappush

import sys
input = sys.stdin.buffer.readline


def main():

    n, q = map(int, input().split())
    stx = [map(int, input().split()) for _ in range(n)]
    ds = [int(input()) for _ in range(q)]
    INF = 10 ** 9 + 1
    CHECK = 2
    START = 1
    END = 0
    NULL = 0

    tfdi = []
    for i, (s, t, x) in enumerate(stx):
        t_start = max(0, s - x)
        t_end = max(0, t - x)

        tfdi.append((t_start, START, x, i))
        tfdi.append((t_end, END, x, i))

    for d in ds:
        tfdi.append((d, CHECK, NULL, NULL))
    tfdi.append((INF, START, INF, -1))
    tfdi.sort()

    hp = [(INF, -1)]
    ans = []
    passed = set()
    for t, f, d, i in tfdi:
        if f == CHECK:
            while hp[0][1] in passed:
                heappop(hp)
            if hp[0][0] == INF:
                tmp = -1
            else:
                tmp = hp[0][0]
            ans.append(tmp)

        elif f == START:
            heappush(hp, (d, i))
        else:
            passed.add(i)

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
