import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    a, b = nm()
    c = max(a, b)
    d = max(c - 1, min(a, b))
    print(c + d)


if __name__ == '__main__':
    main()
