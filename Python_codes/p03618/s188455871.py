import sys
from collections import Counter

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


def main():

    S = list(in_s())
    N = len(S)
    cnt = Counter(S)

    ans = N * (N - 1) // 2 + 1

    orda = ord('a')
    for c in range(orda, orda + 26):
        c = chr(c)
        n = cnt[c]
        ans -= n * (n - 1) // 2

    print(ans)


if __name__ == '__main__':
    main()
