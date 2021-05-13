import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)


def road():
    N = int(input())
    A = tuple(tuple(map(int, input().split())) for _ in range(N))

    res = 0
    for s in range(N - 1):
        for t in range(s + 1, N):
            # s-t間に辺を張るかを決める
            dist = A[s][t]
            is_connect = True
            for m in range(N):
                if m in [s, t]:
                    continue
                d = A[s][m] + A[m][t]
                if d < dist:
                    return -1
                elif d == dist:
                    is_connect = False
            if is_connect:
                res += dist
    return res


if __name__ == "__main__":
    print(road())