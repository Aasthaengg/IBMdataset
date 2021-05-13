import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    X, Y, A, B, C, *PQR = map(int, read().split())
    P = PQR[:A]
    Q = PQR[A : A + B]
    R = PQR[A + B :]

    P.sort(reverse=True)
    Q.sort(reverse=True)
    R.sort()

    P = P[:X]
    Q = Q[:Y]
    S = []

    while R and (P or Q):
        if not P:
            vec = Q
        elif not Q:
            vec = P
        elif P[-1] < Q[-1]:
            vec = P
        else:
            vec = Q

        if vec[-1] < R[-1]:
            S.append(R.pop())
            vec.pop()
        else:
            break

    ans = sum(P) + sum(Q) + sum(S)

    print(ans)
    return


if __name__ == '__main__':
    main()
