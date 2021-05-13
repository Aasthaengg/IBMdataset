import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, q = list(map(int, readline().split()))
    event = [0] * (2 * n + q)

    for i in range(n):
        s, t, x = list(map(int, readline().split()))
        event[i * 2] = (s - x, x, 0)
        event[i * 2 + 1] = (t - x, x, 1)

    for i in range(q):
        d = int(input())
        event[2 * n + i] = (d, 0, 2)

    from operator import itemgetter
    event.sort(key=itemgetter(0))
    stop = set()
    res = INF

    for t, x, ev_type in event:
        if ev_type == 0:
            stop.add(x)
            if res == -1:
                res = x
            elif res > x:
                res = x
        elif ev_type == 1:
            stop.discard(x)
            if res == x:
                if stop:
                    res = min(stop)
                else:
                    res = -1
        else:
            if stop:
                print(res)
            else:
                print(-1)


if __name__ == '__main__':
    main()
