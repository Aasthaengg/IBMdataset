import sys

stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n = ni()
    t, a = nm()
    H = nl()
    D = list(map(lambda x: abs(a - (t - x * 0.006)), H))
    print(D.index(min(D)) + 1)


if __name__ == '__main__':
    main()
