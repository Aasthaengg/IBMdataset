import sys
from operator import itemgetter

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    iPY = [[0] * 3 for _ in range(M)]
    for i in range(M):
        iPY[i][0] = i
        iPY[i][1:] = map(int, input().split())

    iPY.sort(key=itemgetter(2))

    p_count = [0] * (N + 1)
    ans = [""] * M
    for i, P, Y in iPY:
        p_count[P] += 1
        ans[i] = "".join([
            str(P).zfill(6),
            str(p_count[P]).zfill(6)
        ])

    print("\n".join(ans))


if __name__ == "__main__":
    main()
