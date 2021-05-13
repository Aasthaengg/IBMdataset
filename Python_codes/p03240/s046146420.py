import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *XYH = map(int, read().split())

    for x, y, h in zip(*[iter(XYH)] * 3):
        if h != 0:
            x0, y0, h0 = x, y, h

    for cx in range(101):
        for cy in range(101):
            H = h0 + abs(x0 - cx) + abs(y0 - cy)
            ok = True
            for x, y, h in zip(*[iter(XYH)] * 3):
                if max(H - abs(x - cx) - abs(y - cy), 0) != h:
                    ok = False
                    break
            if ok:
                print(cx, cy, H)
                return

    return


if __name__ == '__main__':
    main()
