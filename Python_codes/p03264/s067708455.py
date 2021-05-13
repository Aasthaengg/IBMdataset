import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    k = ni()
    print((k // 2) ** 2 if k % 2 == 0 else (k // 2) * (k // 2 + 1))


if __name__ == '__main__':
    main()
