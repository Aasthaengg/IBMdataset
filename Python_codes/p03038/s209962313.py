import sys
from collections import Counter

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    N, M = map(int, readline().split())
    A = list(map(int, readline().split()))
    BC = list(map(int, read().split()))

    counter = Counter(A)
    for b, c in zip(BC[::2], BC[1::2]):
        counter[c] += b

    ans = cnt = 0
    for n in sorted(counter.keys(), reverse=True):
        if cnt + counter[n] >= N:
            ans += n * (N - cnt)
            break
        else:
            ans += n * counter[n]
            cnt += counter[n]

    print(ans)
    return


if __name__ == '__main__':
    main()
