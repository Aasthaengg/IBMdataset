import sys
import itertools
import bisect

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():

    N = in_n()
    comb = itertools.product([0, 1], repeat=16)

    p = []
    m = []
    for c in comb:
        pt, mt = 0, 0
        for i in range(len(c)):
            pt += c[i] * (4 ** i)
            mt += c[i] * 2 * (4 ** i)
        p.append(pt)
        m.append(mt)

    p.sort()
    m.sort()

    for i in range(len(p)):
        if p[i] < N:
            continue
        else:
            pred_m = -(N - p[i])
            j = bisect.bisect_left(m, pred_m)
            if m[j] == pred_m:
                pred_p = p[i]
                break

    ans = pred_p | pred_m
    print(bin(ans)[2:])


if __name__ == '__main__':
    main()
