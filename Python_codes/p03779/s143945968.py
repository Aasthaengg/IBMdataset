import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    x = ni()
    d = 0
    for i in range(1, x + 1):
        d += i
        if d >= x:
            print(i)
            return


if __name__ == '__main__':
    main()
