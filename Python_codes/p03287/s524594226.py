import sys
from collections import defaultdict

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
    N, M = in_nn()
    A = in_nl()
    total_sum = [0] * (N + 1)

    for i in range(N):
        total_sum[i + 1] = total_sum[i] + A[i]

    for i in range(N + 1):
        total_sum[i] %= M

    d = defaultdict(lambda: 0)
    for i in range(N + 1):
        d[total_sum[i]] += 1

    ans = 0
    for k, v in d.items():
        ans += v * (v - 1) // 2

    print(ans)


if __name__ == '__main__':
    main()
