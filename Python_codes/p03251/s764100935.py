import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n, m, x, y = nm()
    X = nl()
    Y = nl()
    xx = max(X)
    yy = min(Y)
    for z in range(-100, 101):
        if x < z <= y and xx < z <= yy:
            print('No War')
            return
    print('War')


if __name__ == '__main__':
    main()
