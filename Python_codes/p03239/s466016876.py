import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n, T = nm()
    C = []
    for _ in range(n):
        c, t = nm()
        if t <= T:
            C.append(c)
    print(min(C) if C else 'TLE')


if __name__ == '__main__':
    main()
