import sys

input = sys.stdin.readline


def main():
    N = int(input())
    xyh = [None] * N
    for i in range(N):
        xyh[i] = tuple(map(int, input().split()))

    for i in range(N):
        if xyh[i][2] > 0:
            Bx, By, Bh = xyh[i]
            break

    for Cx in range(0, 101):
        for Cy in range(0, 101):
            H = Bh + abs(Bx - Cx) + abs(By - Cy)
            is_ok = True
            for x, y, h in xyh:
                if max(H - abs(x - Cx) - abs(y - Cy), 0) != h:
                    is_ok = False
                    break
            if is_ok:
                print(Cx, Cy, H)
                exit()


if __name__ == "__main__":
    main()
