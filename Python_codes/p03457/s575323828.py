import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    P = [0] * (N + 1)
    P[0] = (0, 0, 0)
    for i in range(1, N + 1):
        P[i] = tuple(map(int, readline().split()))

    ok = True
    for i in range(N):
        dt = P[i + 1][0] - P[i][0]
        dx = P[i + 1][1] - P[i][1]
        dy = P[i + 1][2] - P[i][2]
        if dt < abs(dx) + abs(dy) or (dt - abs(dx) - abs(dy)) % 2 == 1:
            ok = False
            break

    if ok:
        print('Yes')
    else:
        print('No')

    return


if __name__ == '__main__':
    main()
