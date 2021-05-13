import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    d, n = nm()
    if n != 100:
        print(pow(100, d) * n)
    else:
        print(pow(100, d) * 101)


if __name__ == '__main__':
    main()
