import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, M = map(int, readline().split())

    students = []

    for _ in range(N):
        a, b = map(int, readline().split())
        students.append((a, b))

    cp = []
    for _ in range(M):
        c, d = map(int, readline().split())
        cp.append((c, d))

    for i in range(N):
        dist_min = INF
        idx = -1
        x1, y1 = students[i]
        for j in range(M):
            x2, y2 = cp[j]
            dist_cur = abs(x2 - x1) + abs(y2 - y1)
            if dist_cur < dist_min:
                dist_min = dist_cur
                idx = j + 1
        print(idx)


if __name__ == '__main__':
    main()
