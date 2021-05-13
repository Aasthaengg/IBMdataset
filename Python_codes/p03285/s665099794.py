import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n = ni()
    for i in range(100):
        for j in range(100):
            if i * 4 + j * 7 == n:
                print('Yes')
                return
    print('No')


if __name__ == '__main__':
    main()
