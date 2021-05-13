import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    s = input()
    t = input()
    S = sorted(map(s.count, set(s)))
    T = sorted(map(t.count, set(t)))
    print("Yes" if S == T else "No")


if __name__ == '__main__':
    main()
