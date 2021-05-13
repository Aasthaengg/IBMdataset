import sys
import itertools

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    N = in_n()
    S = [0] * 5

    march = ['M', 'A', 'R', 'C', 'H']
    for i in range(N):
        ts = in_s()
        fs = ts[0]
        if fs in march:
            S[march.index(fs)] += 1

    comb = itertools.combinations(range(5), 3)

    ans = 0
    for com in comb:
        t = 1
        for c in com:
            t *= S[c]
        ans += t

    print(ans)


if __name__ == '__main__':
    main()
