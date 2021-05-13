import sys
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    info0 = []
    info1 = []
    for _ in range(N):
        x, y, h = map(int, input().split())
        if h == 0: info0.append((x, y))
        if h != 0: info1.append((x, y, h))

    for cx in range(101):
        for cy in range(101):
            H = -1
            for x, y, h in info1:
                wrong = False
                if h > 0 and H == -1:
                    H = h + abs(cx - x) + abs(cy - y)
                elif h > 0:
                    if H != h + abs(cx - x) + abs(cy - y):
                        wrong = True
                        break
            if wrong: continue
            for x, y in info0:
                wrong = False
                if abs(cx - x) + abs(cy - y) < H:
                    wrong = True
                    break
            if wrong: continue
            print("{} {} {}".format(cx, cy, H))
            exit()

if __name__ == "__main__":
    main()

