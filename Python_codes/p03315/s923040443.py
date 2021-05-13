import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    S = ns()
    ans = '0'
    for s in S:
        ans += s + '1'
    print(eval(ans))


if __name__ == '__main__':
    main()
