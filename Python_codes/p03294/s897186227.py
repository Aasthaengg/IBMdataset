import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n = ni()
    print(sum(list(map(lambda x: x - 1, nl()))))


if __name__ == '__main__':
    main()
