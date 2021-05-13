import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    a, b = nm()
    print('Yay!' if a <= 8 and b <= 8 else ':(')


if __name__ == '__main__':
    main()
