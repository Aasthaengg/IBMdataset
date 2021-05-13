import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)


def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    P = []
    Q = []
    if N == 1:
        print(1)
        return
    for i in range(N - 1):
        for j in range(i + 1, N):
            p = XY[j][0] - XY[i][0]
            q = XY[j][1] - XY[i][1]
            P.append(p)
            Q.append(q)
    ans = float("inf")

    for p, q in zip(P, Q):
        a = N
        for i in range(N):
            x, y = XY[i][0], XY[i][1]
            if [x + p, y + q] in XY:
                a -= 1
        if a < ans:
            ans = a
    print(ans)


if __name__ == "__main__":
    main()
