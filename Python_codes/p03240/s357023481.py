import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *XYH = map(int, read().split())

    for cx in range(101):
        for cy in range(101):
            ok = 10 ** 9 + 100
            ng = 0
            while ok - ng > 1:
                mid = (ok + ng) // 2
                valid = True
                for x, y, h in zip(*[iter(XYH)] * 3):
                    if max(mid - abs(x - cx) - abs(y - cy), 0) < h:
                        valid = False
                        break
                if valid:
                    ok = mid
                else:
                    ng = mid
            H = ok
            valid = True
            for x, y, h in zip(*[iter(XYH)] * 3):
                if max(H - abs(x - cx) - abs(y - cy), 0) != h:
                    valid = False
                    break
            if valid:
                print(cx, cy, H)
                return

    return


if __name__ == '__main__':
    main()
