import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    N = in_n()
    h = in_nl()
    now = [0] * N

    ans = 0
    while h != now:
        ok = [-1] + [i for i, x in enumerate(now) if x == h[i]] + [N]
        lr = []
        for i in range(len(ok) - 1):
            if ok[i + 1] - ok[i] > 1:
                l = ok[i] + 1
                r = ok[i + 1]
                lr.append((l, r))

        for l, r in lr:
            diff = 10**9 + 7
            for i in range(r - l):
                diff = min(diff, h[l + i] - now[l + i])

            ans += diff
            for i in range(r - l):
                now[l + i] += diff

    print(ans)


if __name__ == '__main__':
    main()
