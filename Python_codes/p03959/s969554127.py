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

mod = 10**9 + 7


def main():

    N = in_n()
    A = in_nl()
    T = in_nl()

    if N == 1:
        if A[0] == T[0]:
            print(1)
        else:
            print(0)
        exit()

    yama = [(0, 0)] * N
    yama[0] = (A[0], A[0])

    for i in range(1, N):
        pre_min_h, pre_max_h = yama[i - 1]
        now_h = A[i]

        if pre_max_h < now_h:
            now_min_h = now_h
            now_max_h = now_h
        else:
            now_min_h = 1
            now_max_h = pre_max_h

        yama[i] = (now_min_h, now_max_h)

    yama[-1] = (T[-1], T[-1])

    for i in range(N - 2, -1, -1):

        now_min_h, now_max_h = yama[i]
        pre_h = T[i + 1]
        now_h = T[i]

        if now_h > pre_h:
            if now_min_h <= now_h <= now_max_h:
                now_min_h = now_h
                now_max_h = now_h
            else:
                print(0)
                exit()
        else:
            now_max_h = min(now_max_h, now_h)

        yama[i] = (now_min_h, now_max_h)

    ans = 1
    for i in range(N):
        ans *= (yama[i][1] - yama[i][0] + 1)
        ans %= mod
    print(ans)


if __name__ == '__main__':
    main()
