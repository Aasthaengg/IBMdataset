import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    d = ni()
    ans = 'Christmas'
    num = 25 - d
    eve = ' Eve'
    print(ans + num * eve)


if __name__ == '__main__':
    main()
