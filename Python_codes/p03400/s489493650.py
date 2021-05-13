import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n = ni()
    d, x = nm()
    ans = x
    for i in range(n):
        a = ni()
        ans += (d - 1) // a + 1
    print(ans)


if __name__ == '__main__':
    main()
