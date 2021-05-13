import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    H, W = nm()
    h, w = nm()
    print((H - h) * (W - w))


if __name__ == '__main__':
    main()
