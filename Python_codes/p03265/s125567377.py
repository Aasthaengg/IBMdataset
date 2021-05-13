
def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    x1, y1, x2, y2 = [int(x) for x in input().rstrip().split(" ")]
    x = x2 - x1
    y = y2 - y1
    print(x2 - y, y2 + x, x1 - y, y1 + x)


if __name__ == "__main__":
    resolve()
