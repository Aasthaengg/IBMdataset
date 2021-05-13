import sys

read = sys.stdin.buffer.read


def main():
    N, K, *AF = map(int, read().split())
    A = AF[:N]
    F = AF[N:]

    A.sort()
    F.sort(reverse=True)

    def is_ok(cost):
        k = 0
        for i in range(N):
            if A[i] * F[i] > cost:
                k += (A[i] * F[i] - cost + F[i] - 1) // F[i]
        return k <= K

    ok = pow(10, 12)
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
