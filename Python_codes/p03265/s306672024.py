import sys
input = sys.stdin.readline


def read():
    x1, y1, x2, y2 = map(int, input().strip().split())
    return x1, y1, x2, y2


def solve(x1, y1, x2, y2):
    v12 = (x2-x1, y2-y1)
    v34 = (-x2+x1, -y2+y1)
    v23 = (-y2+y1, x2-x1)
    x3, y3 = x2 + v23[0], y2 + v23[1]
    x4, y4 = x3 + v34[0], y3 + v34[1]
    return "%d %d %d %d" % (x3, y3, x4, y4)


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
