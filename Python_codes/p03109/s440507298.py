import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    y, m, d = input().split('/')
    ymd = int(y + m + d)
    if ymd <= 20190430:
        print('Heisei')
    else:
        print('TBD')


if __name__ == '__main__':
    main()
