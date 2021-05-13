import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n, k = nm()
    A = nl()
    print((n - 1) // (k - 1) if (n - 1) %
          (k - 1) == 0 else (n - 1) // (k - 1) + 1)


if __name__ == '__main__':
    main()
