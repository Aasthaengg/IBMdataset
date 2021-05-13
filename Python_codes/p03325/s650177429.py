import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n = ni()
    A = nl()
    ans = 0
    for a in A:
        while a % 2 == 0:
            a //= 2
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
