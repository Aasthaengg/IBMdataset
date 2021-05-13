import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    R = ni()
    if R < 1200:
        print('ABC')
    elif 1200 <= R < 2800:
        print('ARC')
    else:
        print('AGC')


if __name__ == '__main__':
    main()
