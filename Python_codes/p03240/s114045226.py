import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    xyh = []
    for _ in range(N):
        x, y, h = map(int, input().split())
        xyh.append((x, y, h))

    for cx in range(101):
        for cy in range(101):
            i = 0
            while True:
                x, y, h = xyh[i]
                if h == 0:
                    i += 1
                    continue
                else:
                    H = h + abs(x - cx) + abs(y - cy)
                    break

            for x, y, h in xyh:
                tmp = max(H - abs(x - cx) - abs(y - cy), 0)
                if tmp == h:
                    continue
                else:
                    break
            else:
                print(cx, cy, H)
                return


if __name__ == "__main__":
    main()
