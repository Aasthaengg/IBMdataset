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
    L = in_s()
    N = len(L)

    dp1 = [0] * N
    dp2 = [0] * N

    dp1[0] = 2
    dp2[0] = 1

    for i in range(1, N):
        if L[i] == "0":
            dp1[i] = dp1[i - 1]
            dp2[i] = dp2[i - 1] * 3
        else:
            dp1[i] = dp1[i - 1] * 2
            dp2[i] = dp2[i - 1] * 3 + dp1[i - 1]
        dp1[i] %= mod
        dp2[i] %= mod

    ans = dp1[-1] + dp2[-1]
    ans %= mod

    print(ans)


if __name__ == '__main__':
    main()
