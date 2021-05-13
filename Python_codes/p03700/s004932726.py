import sys

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

INF = 10**9


def main():
    N, A, B = in_nn()
    diff = A - B
    h = list(in_all())

    def is_ok(mid):

        cnt = 0
        for i in range(N):
            x = h[i] - mid * B
            if x > 0:
                cnt += (x + diff - 1) // diff

        return cnt <= mid

    def binary_search(ng, ok):

        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    ans = binary_search(0, INF + 1)
    print(ans)


if __name__ == '__main__':
    main()
