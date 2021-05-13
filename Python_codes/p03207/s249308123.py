import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n = ni()
    P = [ni() for _ in range(n)]
    p = max(P)
    print(sum(P) - p // 2)


if __name__ == '__main__':
    main()
