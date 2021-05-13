import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    x1, y1, x2, y2 = nm()
    print(x2 + y1 - y2, y2 - x1 + x2, y1 - y2 + x1, y1 - x1 + x2)


if __name__ == '__main__':
    main()
