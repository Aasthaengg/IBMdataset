import sys
import itertools

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')

INF = 10**9 + 7


def main():
    N = in_n()
    F = [in_nl() for _ in range(N)]
    P = [in_nl() for _ in range(N)]

    comb = list(itertools.product(range(2), repeat=10))[1:]

    ans = -INF
    for com in comb:
        r = 0
        for i in range(N):
            count = 0
            for j in range(10):
                if F[i][j] == com[j] == 1:
                    count += 1
            r += P[i][count]
        ans = max(ans, r)

    print(ans)


if __name__ == '__main__':
    main()
