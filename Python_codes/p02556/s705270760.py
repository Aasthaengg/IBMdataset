import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n = ni()
    xy = list(nl() for _ in range(n))

    xpy = [x + y for x, y in xy]
    xmy = [x - y for x, y in xy]

    print(max(max(xpy) - min(xpy), max(xmy) - min(xmy)))


if __name__ == '__main__':
    main()
