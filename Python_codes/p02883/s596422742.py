import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K, *AF = map(int, read().split())
    A = AF[:N]
    F = AF[N:]

    A.sort()
    F.sort(reverse=True)
    C = [a * f for a, f in zip(A, F)]

    def is_ok(cost):
        k = 0
        for i in range(N):
            if C[i] > cost:
                k += (C[i] - cost + F[i] - 1) // F[i]
        return k <= K

    ok = max(C)
    ng = -1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid

    print(ok)
    return


if __name__ == '__main__':
    main()
