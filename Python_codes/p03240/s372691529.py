import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():

    N = in_n()
    t = in_na()
    xyh = list(zip(t, t, t))

    for cx in range(101):
        for cy in range(101):
            hmax = 10**9 + 7
            pred_h = -1
            for i in range(N):
                x, y, h = xyh[i]
                xy = abs(x - cx) + abs(y - cy)
                if h == 0:
                    hmax = min(hmax, xy)
                    if pred_h > hmax:
                        break
                else:
                    if pred_h == -1:
                        pred_h = h + xy
                    elif pred_h != h + xy:
                        break
            else:
                print(cx, cy, pred_h)
                exit()


if __name__ == '__main__':
    main()
