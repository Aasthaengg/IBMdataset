import sys
def input(): return sys.stdin.readline().strip()


def main():
    x1, y1, x2, y2 = map(int, input().split())
    vec = (x2 - x1, y2 - y1)
    x3, y3 = x2 - vec[1], y2 + vec[0]
    x4, y4 = x3 - vec[0], y3 - vec[1]
    print("{} {} {} {}".format(x3, y3, x4, y4))


if __name__ == "__main__":
    main()
